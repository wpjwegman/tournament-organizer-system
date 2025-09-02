# Validation Script for Tournament Organizer Documentation
# PowerShell script to run all quality checks locally

param(
    [switch]$Fix,
    [switch]$Verbose,
    [switch]$Help
)

function Show-Help {
    Write-Host "Tournament Organizer Documentation Validation" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage: .\validate-docs.ps1 [OPTIONS]"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Fix       Automatically fix issues where possible"
    Write-Host "  -Verbose   Show detailed output"
    Write-Host "  -Help      Show this help message"
    Write-Host ""
    Write-Host "This script runs the same checks as the CI/CD pipeline:"
    Write-Host "  • Markdown linting (PyMarkdown)"
    Write-Host "  • YAML validation"
    Write-Host "  • Navigation orphan detection"
    Write-Host "  • Frontmatter title verification"
    Write-Host "  • MkDocs build test"
    Write-Host ""
}

function Test-Prerequisites {
    Write-Host "Checking prerequisites..." -ForegroundColor Yellow

    # Check if we're in the right directory
    if (-not (Test-Path "documents/mkdocs.yml")) {
        Write-Host "Error: Must be run from project root directory" -ForegroundColor Red
        return $false
    }

    # Check if uv is available
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Host "Error: uv not found. Run setup.ps1 first." -ForegroundColor Red
        return $false
    }

    return $true
}

function Invoke-PreCommitChecks {
    Write-Host "Running pre-commit hooks..." -ForegroundColor Blue
    Set-Location documents

    try {
        if ($Fix) {
            uv run pre-commit run --all-files
        } else {
            uv run pre-commit run --all-files --show-diff-on-failure
        }

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Pre-commit hooks passed" -ForegroundColor Green
        } else {
            Write-Host "❌ Pre-commit hooks failed" -ForegroundColor Red
        }
    } finally {
        Set-Location ..
    }
}

function Test-NavigationOrphans {
    Write-Host "Checking for navigation orphans..." -ForegroundColor Blue
    Set-Location documents

    try {
        uv run python scripts/check_nav_orphans.py

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ No navigation orphans found" -ForegroundColor Green
        } else {
            Write-Host "❌ Navigation orphans detected" -ForegroundColor Red
        }
    } finally {
        Set-Location ..
    }
}

function Test-FrontmatterTitles {
    Write-Host "Checking frontmatter titles..." -ForegroundColor Blue
    Set-Location documents

    try {
        uv run python scripts/check_no_frontmatter_title.py

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ No problematic frontmatter titles found" -ForegroundColor Green
        } else {
            Write-Host "❌ Frontmatter title issues detected" -ForegroundColor Red
        }
    } finally {
        Set-Location ..
    }
}

function Test-MkDocsBuild {
    Write-Host "Testing MkDocs build..." -ForegroundColor Blue
    Set-Location documents

    try {
        if ($Verbose) {
            uv run mkdocs build --clean --strict --verbose
        } else {
            uv run mkdocs build --clean --strict
        }

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ MkDocs build successful" -ForegroundColor Green
        } else {
            Write-Host "❌ MkDocs build failed" -ForegroundColor Red
        }
    } finally {
        Set-Location ..
    }
}

function Main {
    if ($Help) {
        Show-Help
        return
    }

    Write-Host "Tournament Organizer Documentation Validation" -ForegroundColor Green
    Write-Host "=============================================" -ForegroundColor Green
    Write-Host ""

    if (-not (Test-Prerequisites)) {
        return
    }

    $startTime = Get-Date
    $totalErrors = 0

    # Run all validation checks
    Invoke-PreCommitChecks
    if ($LASTEXITCODE -ne 0) { $totalErrors++ }

    Test-NavigationOrphans
    if ($LASTEXITCODE -ne 0) { $totalErrors++ }

    Test-FrontmatterTitles
    if ($LASTEXITCODE -ne 0) { $totalErrors++ }

    Test-MkDocsBuild
    if ($LASTEXITCODE -ne 0) { $totalErrors++ }

    # Summary
    $endTime = Get-Date
    $duration = $endTime - $startTime

    Write-Host ""
    Write-Host "Validation Summary" -ForegroundColor Yellow
    Write-Host "=================" -ForegroundColor Yellow
    Write-Host "Duration: $($duration.TotalSeconds.ToString('F1')) seconds"

    if ($totalErrors -eq 0) {
        Write-Host "🎉 All checks passed! Documentation is ready." -ForegroundColor Green
    } else {
        Write-Host "⚠️  $totalErrors check(s) failed. Please fix the issues above." -ForegroundColor Red
    }
}

# Run main function
Main
