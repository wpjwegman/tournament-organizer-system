# Enterprise Markdown Linting Setup

This project uses an enterprise-grade markdown linting and fixing system with the following components:

## 🎯 Core Components

### 1. markdownlint-cli2 (Primary Linter)

- **Industry standard** Node.js-based markdown linter
- **Zero false positives** with YAML frontmatter
- **Fast and reliable** with excellent VS Code integration
- **Installation**: `npm install -g markdownlint-cli2`

### 2. Custom Domain-Specific Fixers

- **MD007**: Unordered list indentation
- **MD012**: Multiple consecutive blank lines
- **MD022**: Headings surrounded by blank lines
- **MD025**: Multiple top-level headings
- **MD031**: Fenced code blocks surrounded by blank lines
- **MD032**: Lists surrounded by blank lines
- **MD041**: First line in file should be a top-level heading
- **MD047**: Files should end with a single newline

### 3. Orchestrator (`run_all_md_fixes.py`)

- **Before/after reporting** with error counts
- **Domain-specific execution** (e.g., identity, finance)
- **Professional logging** and change tracking
- **Pre-commit integration** ready

## 🚀 Usage

### Command Line

```bash

# Lint a specific domain
uv run python documents/scripts/linting/domain_linter.py identity --check-only --verbose

# Fix all errors in a domain
uv run python scripts/linting/md_fixes/run_all_md_fixes.py . identity

# Test with markdownlint-cli2 directly
markdownlint-cli2 documents/docs/domains/identity/**/*.md

```

### Pre-commit Integration

```bash

# Install pre-commit hooks
pre-commit install

# Run manually
pre-commit run --all-files

# Test specific hook
pre-commit run markdownlint-cli2 --all-files

```

## 📁 Configuration Files

### `.markdownlint.json`

Enterprise-grade configuration with proper YAML frontmatter support.

### `.pre-commit-config.yaml`

- **markdownlint-cli2** for primary linting
- **Custom domain fixers** for specialized rules
- **Ruff** for Python code quality
- **Standard hooks** for file consistency

## 🎉 Migration Complete

✅ **Replaced** pymarkdownlnt with markdownlint-cli2
✅ **Eliminated** false positives with YAML frontmatter
✅ **Enhanced** pre-commit integration with enterprise hooks
✅ **Modernized** configuration with industry standards
✅ **Improved** performance and reliability

The system is now ready for enterprise-level documentation quality assurance.
