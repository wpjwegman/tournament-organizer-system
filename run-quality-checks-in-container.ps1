# PowerShell script: run-quality-checks-in-container.ps1
# Automates running pre-commit hooks and quality tools in a Podman container with mounted code

# Build the container (if not already built)
podman build -f documents/Containerfile -t docs-quality:latest documents

# Run the container interactively, mounting the project
podman run --rm -it -v ${PWD}:/workspace -w /workspace/documents docs-quality:latest pwsh -c @'
    # Activate Python environment if needed
    if (Test-Path .venv/Scripts/Activate.ps1) { . .venv/Scripts/Activate.ps1 }
    # Run pre-commit hooks
    uv run pre-commit run --all-files
    # Run domain linting and validation scripts
    uv run python scripts/validation/check_nav_orphans.py
    uv run python scripts/linting/domain_linter.py --check-only
    uv run python scripts/linting/repository_linter.py --all-domains --report
    # Optionally, run markdownlint directly
    markdownlint-cli2 "docs/**/*.md"
'
