# Tournament Organizer Scripts

This directory contains development and quality assurance scripts for the Tournament Organizer System.

## Directory Structure

### `container/`
Container management scripts for the documentation environment.
- `build.ps1` - Build the validation container image
- `validate.ps1` - Run quality checks in container

### `validation/`
Python validation scripts for documentation quality.
- `check_nav_orphans.py` - Ensure all pages are included in navigation
- `check_no_frontmatter_title.py` - Validate frontmatter structure

### `linting/`
Code quality and markdown linting tools.
- Domain-specific linters and formatters
- Pre-commit integration scripts
- Markdown fixing utilities

### `git-hooks/`
Git hooks for automated quality checks.
- Pre-commit domain linting scripts
- Git hooks setup utilities

### `cli/`
Command-line interface tools for manual operations.

### `legacy/`
Archived scripts and configurations for reference.

## Quick Start

For the container-based validation workflow:

```powershell
# Build container (one-time setup)
.\container\build.ps1

# Run validation
.\container\validate.ps1
```

## Requirements

- PowerShell (cross-platform)
- Podman (Windows) or Docker (Linux/macOS)
- Python 3.13+ (for local script execution)

## Usage Patterns

1. **Container-based validation** (recommended): Use `container/` scripts
2. **Local validation**: Use `validation/` and `linting/` scripts directly
3. **CI/CD integration**: Leverage git hooks from `git-hooks/`
4. **Manual operations**: Use tools from `cli/`