# Development Setup Script for Tournament Organizer
# PowerShell script to set up local development environment

param(
    [switch]$Docs,
    [switch]$Backend,
    [switch]$Frontend,
    [switch]$All,
    [switch]$Help
)

function Show-Help {
    Write-Host "Tournament Organizer Development Setup" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage: .\setup.ps1 [OPTIONS]"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Docs      Set up documentation environment (MkDocs)"
    Write-Host "  -Backend   Set up backend environment (FastAPI) [Coming Soon]"
    Write-Host "  -Frontend  Set up frontend environment (React) [Coming Soon]"
    Write-Host "  -All       Set up all environments"
    Write-Host "  -Help      Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  .\setup.ps1 -Docs                # Setup documentation only"
    Write-Host "  .\setup.ps1 -All                 # Setup everything"
    Write-Host ""
}

function Setup-Documentation {
    Write-Host "Setting up documentation environment..." -ForegroundColor Yellow
    
    # Check if uv is installed
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Host "Installing uv (Python package manager)..." -ForegroundColor Blue
        Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression
    }
    
    # Navigate to documents directory
    Set-Location documents
    
    # Install Python and dependencies
    Write-Host "Installing Python and dependencies..." -ForegroundColor Blue
    uv sync
    
    # Install pre-commit hooks
    Write-Host "Installing pre-commit hooks..." -ForegroundColor Blue
    uv run pre-commit install
    
    # Test documentation build
    Write-Host "Testing documentation build..." -ForegroundColor Blue
    uv run mkdocs build --clean
    
    Write-Host "Documentation environment setup complete!" -ForegroundColor Green
    Write-Host ""
    Write-Host "To serve documentation locally:"
    Write-Host "  Set-Location documents"
    Write-Host "  uv run mkdocs serve"
    Write-Host ""
    
    Set-Location ..
}

function Setup-Backend {
    Write-Host "Backend setup coming soon..." -ForegroundColor Yellow
    Write-Host "Backend development will begin after domain documentation is complete."
}

function Setup-Frontend {
    Write-Host "Frontend setup coming soon..." -ForegroundColor Yellow
    Write-Host "Frontend development will begin after backend API is available."
}

function Main {
    if ($Help) {
        Show-Help
        return
    }
    
    if (-not ($Docs -or $Backend -or $Frontend -or $All)) {
        Write-Host "No options specified. Use -Help for usage information." -ForegroundColor Red
        return
    }
    
    Write-Host "Tournament Organizer Development Setup" -ForegroundColor Green
    Write-Host "=======================================" -ForegroundColor Green
    Write-Host ""
    
    if ($All -or $Docs) {
        Setup-Documentation
    }
    
    if ($All -or $Backend) {
        Setup-Backend
    }
    
    if ($All -or $Frontend) {
        Setup-Frontend
    }
    
    Write-Host "Setup complete! Happy coding! 🚀" -ForegroundColor Green
}

# Run main function
Main
