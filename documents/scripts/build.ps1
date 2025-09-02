# build.ps1 - Builds the Podman container image for the documentation environment.

# Stop script execution on any error
$ErrorActionPreference = "Stop"

# --- Configuration ---
$ContainerImage = "localhost/docs-quality:latest"
# The script is in documents/scripts. The project root is two levels up.
$ProjectRoot = (Resolve-Path "$PSScriptRoot\..\..").Path
$DocumentsRoot = (Resolve-Path "$PSScriptRoot\..").Path
$ContainerfilePath = Join-Path $DocumentsRoot "Containerfile"

# --- Script Body ---

Write-Host "🚀 Starting container build workflow..." -ForegroundColor Green

# 1. Build the Podman container image
Write-Host "🏗️ Building container image '$ContainerImage'..." -ForegroundColor Cyan
try {
    # Set the build context explicitly to the 'documents' directory
    podman build --file "$ContainerfilePath" --tag $ContainerImage "$DocumentsRoot"
    Write-Host "✅ Container image built successfully." -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to build container image. Please check Podman and the Containerfile." -ForegroundColor Red
    exit 1
}

Write-Host "🎉 Container build workflow completed." -ForegroundColor Green
