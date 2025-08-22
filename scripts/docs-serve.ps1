# Documentation Server Script for Tournament Organizer
# PowerShell script to serve documentation locally

param(
    [int]$Port = 8000,
    [switch]$Open,
    [switch]$Help
)

function Show-Help {
    Write-Host "Tournament Organizer Documentation Server" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage: .\docs-serve.ps1 [OPTIONS]"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Port <number>  Port to serve on (default: 8000)"
    Write-Host "  -Open           Automatically open browser"
    Write-Host "  -Help           Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  .\docs-serve.ps1                # Serve on port 8000"
    Write-Host "  .\docs-serve.ps1 -Port 3000     # Serve on port 3000"
    Write-Host "  .\docs-serve.ps1 -Open          # Serve and open browser"
    Write-Host ""
}

function Start-DocumentationServer {
    Write-Host "Starting documentation server..." -ForegroundColor Yellow
    
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
        $url = "http://localhost:$Port"
        
        Write-Host "🚀 Starting MkDocs server on $url" -ForegroundColor Green
        Write-Host ""
        Write-Host "Press Ctrl+C to stop the server"
        Write-Host ""
        
        # Open browser if requested
        if ($Open) {
            Start-Sleep -Seconds 2
            Start-Process $url
        }
        
        # Start the server
        uv run mkdocs serve --dev-addr "127.0.0.1:$Port"
        
    } catch {
        Write-Host "Error starting server: $_" -ForegroundColor Red
    } finally {
        Set-Location ..
    }
}

function Main {
    if ($Help) {
        Show-Help
        return
    }
    
    Write-Host "Tournament Organizer Documentation Server" -ForegroundColor Green
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host ""
    
    Start-DocumentationServer
}

# Run main function
Main
