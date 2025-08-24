# Documentation Build Script for Tournament Organizer
# PowerShell script to build static documentation

param(
    [string]$OutputPath = "docs-export",
    [switch]$Open,
    [switch]$Help
)

function Show-Help {
    Write-Host "Tournament Organizer Documentation Builder" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage: .\docs-build.ps1 [OPTIONS]"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -OutputPath <path>  Output directory (default: docs-export)"
    Write-Host "  -Open               Open built documentation"
    Write-Host "  -Help               Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  .\docs-build.ps1                           # Build to docs-export/"
    Write-Host "  .\docs-build.ps1 -OutputPath my-docs      # Build to my-docs/"
    Write-Host "  .\docs-build.ps1 -Open                    # Build and open"
    Write-Host ""
}

function Build-Documentation {
    Write-Host "Building static documentation..." -ForegroundColor Yellow
    
    # Check if we're in the right directory
    if (-not (Test-Path "documents/mkdocs.yml")) {
        Write-Host "Error: Must be run from project root directory" -ForegroundColor Red
        return
    }
    
    # Check if uv is available
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Host "Error: uv not found. Run setup.ps1 first." -ForegroundColor Red
        return
    }
    
    # Navigate to documents directory
    Set-Location documents
    
    try {
        Write-Host "🏗️  Building documentation site..." -ForegroundColor Green
        
        # Build the documentation
        uv run mkdocs build --site-dir "../$OutputPath"
        
        Write-Host ""
        Write-Host "✅ Documentation built successfully!" -ForegroundColor Green
        Write-Host "📁 Location: $((Resolve-Path "../$OutputPath").Path)" -ForegroundColor Cyan
        Write-Host ""
        
        # Open if requested
        if ($Open) {
            $indexPath = "../$OutputPath/index.html"
            if (Test-Path $indexPath) {
                Write-Host "🚀 Opening documentation..." -ForegroundColor Yellow
                Start-Process (Resolve-Path $indexPath).Path
            }
        }
        
    } catch {
        Write-Host "Error building documentation: $_" -ForegroundColor Red
    } finally {
        Set-Location ..
    }
}

function Main {
    if ($Help) {
        Show-Help
        return
    }
    
    Write-Host "Tournament Organizer Documentation Builder" -ForegroundColor Green
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host ""
    
    Build-Documentation
}

# Run main function
Main
