# PowerShell script to fix markdown linting issues
# Usage: .\fix-markdown-lint.ps1

param(
    [string]$Domain = "finance",
    [switch]$CheckOnly,
    [switch]$AllDomains,
    [switch]$AllFiles
)

Set-Location "C:\Projects\Tournament Organizer\documents"

if ($AllFiles) {
    $targetPath = "**/*.md"
    Write-Host "Processing ALL markdown files in the repository..." -ForegroundColor Green
} elseif ($AllDomains) {
    $targetPath = "docs\domains\**\*.md"
    Write-Host "Processing all domain markdown files..." -ForegroundColor Green
} else {
    $targetPath = "docs\domains\$Domain\*.md"
    Write-Host "Processing $Domain domain markdown files..." -ForegroundColor Green
}

if (-not $CheckOnly) {
    Write-Host "`nFixing markdown issues..." -ForegroundColor Yellow
    
    if ($AllFiles) {
        # For all files, use recursive search
        Get-ChildItem -Path . -Recurse -Filter "*.md" | ForEach-Object {
            Write-Host "Processing $($_.FullName.Replace((Get-Location).Path + '\', ''))..." -ForegroundColor Cyan
            python scripts\fix_markdown_lint.py $_.FullName
        }
    } else {
        Get-ChildItem $targetPath | ForEach-Object {
            Write-Host "Processing $($_.Name)..." -ForegroundColor Cyan
            python scripts\fix_markdown_lint.py $_.FullName
        }
    }
}

Write-Host "`nRunning lint check with CORRECT configuration..." -ForegroundColor Yellow
if ($AllFiles) {
    Write-Host "Checking entire repository (this may take a while)..." -ForegroundColor Cyan
    uv run pymarkdownlnt --config .pymarkdown.json scan . --recurse
} elseif ($AllDomains) {
    uv run pymarkdownlnt --config .pymarkdown.json scan docs\domains\ --recurse
} else {
    uv run pymarkdownlnt --config .pymarkdown.json scan "docs\domains\$Domain\"
}

Write-Host "`nCompleted!" -ForegroundColor Green
