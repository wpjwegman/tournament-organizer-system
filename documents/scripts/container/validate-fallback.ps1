# validate-fallback.ps1 - Local validation when container has issues
# This script runs quality checks locally when the container environment has problems

$ErrorActionPreference = "Stop"

Write-Host "🚀 Starting local validation workflow..." -ForegroundColor Green
Write-Host "   (Using local environment as fallback)" -ForegroundColor Yellow

$ProjectRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path
$DocumentsPath = Join-Path $ProjectRoot "documents"

# Change to documents directory
Push-Location $DocumentsPath

try {
    Write-Host ""
    Write-Host "🔒 Security scanning with Bandit..." -ForegroundColor Cyan
    .venv\Scripts\activate
    bandit -r scripts/ --configfile pyproject.toml -f screen
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Security scan passed" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Security issues found - review required" -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "🎯 Code quality analysis with Ruff..." -ForegroundColor Cyan
    ruff check scripts/
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Code quality passed" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Code quality issues found - review required" -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "📚 Documentation validation..." -ForegroundColor Cyan
    markdownlint-cli2 "docs/**/*.md"
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Documentation validation passed" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Documentation issues found - review required" -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "🏆 Running quality dashboard..." -ForegroundColor Cyan
    python scripts/validation/quality_dashboard.py --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Quality dashboard completed" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Quality dashboard completed with warnings" -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "✅ Local validation workflow completed!" -ForegroundColor Green

} catch {
    Write-Host "❌ Validation failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
} finally {
    Pop-Location
}
