# Container Management Scripts

This directory contains scripts for managing the containerized development environment.

## Scripts

### `build.ps1`

Builds the Podman container image for the documentation environment.

**Usage:**

```powershell
.\build.ps1
```

**What it does:**

- Builds `localhost/docs-quality:latest` container image
- Installs Python 3.13, Node.js, markdownlint-cli2, uv, and project dependencies
- Creates a consistent validation environment

### `validate.ps1`

Runs all quality checks inside the pre-built Podman container.

**Usage:**

```powershell
.\validate.ps1
```

**What it does:**

- Executes markdownlint-cli2 validation on all documentation
- Uses your local files while running in consistent container environment
- Reports formatting and style issues
- Provides clear error reporting and exit codes

## Quick Start

1. **Build the container** (one-time setup):

   ```powershell
   .\build.ps1
   ```

2. **Run validation**:

   ```powershell
   .\validate.ps1
   ```

## Requirements

- Podman (Windows) or Docker (Linux/macOS)
- PowerShell (cross-platform)

## Container Details

- **Base Image**: `python:3.13-slim`
- **Tools**: markdownlint-cli2, uv, pre-commit, ruff
- **Working Directory**: `/workspace/documents`
- **User**: `tournament` (non-root)
