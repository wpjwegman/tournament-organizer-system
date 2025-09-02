# Tournament Organizer Scripts

This directory contains development and quality assurance scripts for the Tournament Organizer System.

## Directory Structure

### `container/`

Container management scripts for the documentation environment.

- `build.ps1` - Build the validation container image
- `validate.ps1` - Run quality checks in container

### `validation/`

Python validation scripts for documentation quality and comprehensive quality control.

- `check_nav_orphans.py` - Ensure all pages are included in navigation
- `check_no_frontmatter_title.py` - Validate frontmatter structure
- `quality_dashboard.py` - Professional quality metrics and reporting
- `ci_issue_resolver.py` - Automated CI/CD issue resolution

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

- `quick_quality.py` - Quick quality control commands

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

## 🏆 Quality Control System

Professional quality monitoring and automation:

### 🚀 Quick Start

```bash
# Daily quality check
uv run python scripts/cli/quick_quality.py check

# Auto-fix common issues  
uv run python scripts/cli/quick_quality.py fix

# View quality dashboard
uv run python scripts/cli/quick_quality.py dashboard

# Security analysis only
uv run python scripts/cli/quick_quality.py security
```

### 🔧 Advanced Tools

- **`validation/quality_dashboard.py`** - Comprehensive quality metrics and reporting
- **`validation/ci_issue_resolver.py`** - Automated CI/CD issue resolution
- **Pre-commit hooks** - Automatic quality checks on commit
- **Container workflow** - Consistent validation environment

### 📊 Quality Metrics

The system monitors:

- 🔒 **Security**: Bandit vulnerability scanning
- 🎯 **Code Quality**: Ruff style and complexity analysis  
- 🔍 **Type Safety**: MyPy static type checking
- 🧪 **Test Coverage**: Pytest with coverage reporting
- 📚 **Documentation**: markdownlint-cli2 formatting
- 🏗️ **Complexity**: Radon code complexity analysis
