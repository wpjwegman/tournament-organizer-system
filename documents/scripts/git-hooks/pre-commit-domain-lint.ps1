# PowerShell pre-commit hook for domain-specific markdown linting
# Place this in .git/hooks/pre-commit.ps1 and configure Git to use it

param()

# Configuration
$DocumentsDir = "documents"
$DomainLintScript = "scripts/linting/domain_linter.py"

Write-Host "🔍 Running domain-specific markdown linting..." -ForegroundColor Green

# Get list of modified .md files in docs/domains/
$modifiedFiles = git diff --cached --name-only --diff-filter=ACM | Where-Object { $_ -match '^documents/docs/domains/.*\.md$' }

if (-not $modifiedFiles) {
    Write-Host "✅ No domain markdown files modified" -ForegroundColor Green
    exit 0
}

# Extract unique domains from modified files
$domains = $modifiedFiles | ForEach-Object { 
    if ($_ -match '^documents/docs/domains/([^/]*)/') { 
        $Matches[1] 
    } 
} | Sort-Object -Unique

Write-Host "📁 Modified domains: $($domains -join ', ')" -ForegroundColor Yellow

# Check each domain
$failedDomains = @()
Push-Location $DocumentsDir

foreach ($domain in $domains) {
    Write-Host "`n🎯 Checking $domain domain..." -ForegroundColor Yellow
    
    # Run domain linting with threshold (allow some errors for domains under development)
    python $DomainLintScript $domain --check-only --threshold 10 | Out-Null
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ $domain domain passed" -ForegroundColor Green
    } else {
        Write-Host "❌ $domain domain failed linting" -ForegroundColor Red
        Write-Host "💡 Run: python $DomainLintScript $domain --fix --auto-stage" -ForegroundColor Yellow
        $failedDomains += $domain
    }
}

Pop-Location

# Check if any domains failed
if ($failedDomains.Count -gt 0) {
    Write-Host "`n❌ Commit blocked due to linting failures in: $($failedDomains -join ', ')" -ForegroundColor Red
    Write-Host "Fix the issues and try again." -ForegroundColor Yellow
    exit 1
}

Write-Host "`n🎉 All domain markdown files pass linting!" -ForegroundColor Green
exit 0
