# validate.ps1 - Runs all quality checks inside the pre-built Podman container.
# This script ensures a consistent validation environment.

# Stop script execution on any error
$ErrorActionPreference = "Stop"

# --- Configuration ---
$ContainerImage = "localhost/docs-quality:latest"
# The script is in documents/scripts. The project root is two levels up.
$ProjectRoot = (Resolve-Path "$PSScriptRoot\..\..").Path

# --- Script Body ---

Write-Host "🚀 Starting validation workflow..." -ForegroundColor Green

# 1. Define the validation commands to be executed inside the container
# Using a here-string for multi-line command clarity
$ValidationCommands = @"
echo '--- Running core validation checks ---'
echo 'Validating markdown formatting with markdownlint-cli2...'
markdownlint-cli2 "docs/**/*.md"
echo 'Validation checks completed.'
"@

# 2. Run the validation commands in the container
Write-Host "🔍 Running validation commands in container..." -ForegroundColor Cyan
Write-Host "   (This will use your local files. Fix any reported errors in your editor and re-run this script.)"

# Run the podman command and capture the exit code
$podmanExitCode = 0
try {
    # Mounts the project root to /workspace and sets the working directory to /workspace/documents
    podman run --pull=never --rm -v "${ProjectRoot}:/workspace" -w /workspace/documents $ContainerImage bash -c "$ValidationCommands"
    $podmanExitCode = $LASTEXITCODE
} catch {
    $podmanExitCode = 1
    Write-Host "❌ Container execution failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Check the exit code and report results
if ($podmanExitCode -eq 0) {
    Write-Host "✅ All validation checks passed successfully!" -ForegroundColor Green
    Write-Host "🎉 Validation workflow completed." -ForegroundColor Green
} else {
    Write-Host "❌ Validation failed with exit code: $podmanExitCode" -ForegroundColor Red
    Write-Host "   Please review the errors above, fix them locally, and re-run this script." -ForegroundColor Yellow
    exit $podmanExitCode
}