# Professional Documentation Scripts

This directory contains a comprehensive suite of professional scripts for markdown documentation quality control, linting, and Git workflow integration.

## 📁 Directory Structure

```
scripts/
├── README.md                     # This file
├── cli/                         # Command-line interfaces
│   ├── domain-lint.bat         # Windows CLI for domain linting
│   ├── domain-lint.sh          # Unix CLI for domain linting
│   ├── lint-docs.bat          # Legacy batch script
│   └── lint_cli.py            # Unified Python CLI (in development)
├── git-hooks/                   # Git integration
│   ├── pre-commit-domain-lint.ps1  # PowerShell pre-commit hook
│   ├── pre-commit-domain-lint.sh   # Bash pre-commit hook
│   └── setup_git_hooks.py         # Git hooks management
├── linting/                     # Core linting functionality
│   ├── domain_linter.py        # Per-domain markdown linting
│   ├── repository_linter.py    # Repository-wide linting
│   ├── markdown_fixer.py       # Automatic markdown fixing
│   ├── legacy_autofix.py       # Legacy auto-fix script
│   ├── fix-finance-lint.bat    # Legacy finance domain script
│   ├── fix-finance-lint.ps1    # Legacy PowerShell script
│   └── fix-markdown-lint.ps1   # Legacy PowerShell fixer
└── validation/                  # Content validation
    ├── check_nav_orphans.py    # Navigation validation
    └── check_no_frontmatter_title.py  # YAML frontmatter validation
```

## � GitHub Workflow Integration

The professional linting scripts are fully integrated with GitHub Actions for enterprise-grade quality control:

### 📊 Automated Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| **Documentation Quality Control** | PR/Push to main | Strict validation (0 errors) |
| **Pre-Commit Validation** | PR events | Development validation (5 errors/domain) |
| **Automated Quality Reports** | Weekly schedule | Comprehensive monitoring & auto-fix |

### 🎯 Workflow Features

**✅ Pull Request Validation:**
- Automatic domain-specific linting on every PR
- Same rules as local pre-commit hooks
- Auto-fix capability with `auto-fix-docs` label
- Detailed reports with fix suggestions

**✅ Continuous Monitoring:**
- Weekly quality dashboard generation
- Domain-specific quality scores
- Automated issue creation for quality problems
- Trend analysis and improvement tracking

**✅ Developer Experience:**
- Immediate feedback on documentation changes
- Consistent local and CI environments
- Clear fix guidance and automated suggestions
- Non-blocking development workflow with appropriate thresholds

### 🔧 Local Setup for GitHub Integration

```bash
# Install pre-commit hooks (matches CI validation)
cd documents
python scripts/git-hooks/setup_git_hooks.py --install

# Verify integration
git add .
git commit -m "Test commit"  # Triggers local validation
```

### 📊 Quality Monitoring

**Weekly Reports Include:**
- Repository-wide error statistics
- Domain-specific quality scores  
- Error trend analysis
- Automated fix recommendations

**Access Methods:**
- GitHub Actions artifacts (90-day retention)
- Automatic GitHub issues for problems
- Weekly dashboard in repository

For complete GitHub integration details, see: [`../.github/WORKFLOW_INTEGRATION.md`](../.github/WORKFLOW_INTEGRATION.md)

## �🚀 Quick Start

### Domain-Specific Linting

For Windows (PowerShell):
```powershell
# Check a domain for linting issues
.\scripts\cli\domain-lint.bat finance

# Fix issues and auto-stage changes
.\scripts\cli\domain-lint.bat finance fix

# Generate detailed report
.\scripts\cli\domain-lint.bat finance report
```

For Unix/Linux:
```bash
# Check a domain for linting issues
./scripts/cli/domain-lint.sh finance

# Fix issues and auto-stage changes
./scripts/cli/domain-lint.sh finance fix

# Generate detailed report
./scripts/cli/domain-lint.sh finance report
```

### Repository-Wide Operations

```python
# Lint all domain files
python scripts/linting/repository_linter.py --all-domains --report

# Fix all issues and generate report
python scripts/linting/repository_linter.py --all-domains --fix --save-report

# Process entire repository
python scripts/linting/repository_linter.py --fix --verbose
```

### Git Hook Integration

```python
# Install pre-commit hooks
python scripts/git-hooks/setup_git_hooks.py --install

# Check hook status
python scripts/git-hooks/setup_git_hooks.py --status

# Uninstall hooks
python scripts/git-hooks/setup_git_hooks.py --uninstall
```

## 🎯 Core Scripts

### 1. Domain Linter (`linting/domain_linter.py`)

Professional per-domain markdown linting with Git integration.

**Features:**
- Domain-specific file processing
- Configurable error thresholds
- Automatic fixing capabilities
- Git staging integration
- Professional reporting

**Usage:**
```python
python scripts/linting/domain_linter.py finance --fix --auto-stage --verbose
python scripts/linting/domain_linter.py tournament --check-only --report
python scripts/linting/domain_linter.py identity --check-only --max-errors 5
```

### 2. Repository Linter (`linting/repository_linter.py`)

Comprehensive repository-wide markdown analysis and fixing.

**Features:**
- Batch processing with progress tracking
- Detailed statistics and error categorization
- Export capabilities
- Cross-domain analysis

**Usage:**
```python
python scripts/linting/repository_linter.py --all-domains --report
python scripts/linting/repository_linter.py --fix --verbose --save-report
```

### 3. Markdown Fixer (`linting/markdown_fixer.py`)

Automated fixing tool for common markdown linting issues.

**Features:**
- MD032: Lists surrounded by blank lines
- MD012: Multiple consecutive blank lines
- YAML frontmatter formatting
- Heading spacing fixes

**Usage:**
```python
python scripts/linting/markdown_fixer.py docs/domains/finance/README.md
```

### 4. Git Hooks Manager (`git-hooks/setup_git_hooks.py`)

Professional Git hooks installation and management.

**Features:**
- Cross-platform hook installation
- Automatic backup and restore
- Professional error handling
- Status reporting

**Usage:**
```python
python scripts/git-hooks/setup_git_hooks.py --install
python scripts/git-hooks/setup_git_hooks.py --status
```

## 🔧 Configuration

All scripts use the repository's `.pymarkdown.json` configuration file:

```json
{
  "extensions": {
    "front-matter": {
      "enabled": true
    }
  },
  "plugins": {
    "MD013": {
      "enabled": true,
      "line_length": 120
    },
    "MD032": {
      "enabled": true
    }
  }
}
```

## 🎭 Workflow Integration

### Pre-Commit Workflow

1. **Install hooks:** `python scripts/git-hooks/setup_git_hooks.py --install`
2. **Make changes** to domain documentation
3. **Stage changes:** `git add .`
4. **Commit:** `git commit -m "Update finance domain"`
5. **Automatic linting** runs on modified domains
6. **Fix issues** if needed: Domain-specific error thresholds prevent blocking

### Development Workflow

1. **Check domain status:** `./scripts/cli/domain-lint.bat finance`
2. **Fix issues:** `./scripts/cli/domain-lint.bat finance fix`
3. **Generate report:** `./scripts/cli/domain-lint.bat finance report`
4. **Commit changes:** Normal Git workflow with automatic pre-commit validation

### Quality Control Workflow

1. **Repository analysis:** `python scripts/linting/repository_linter.py --all-domains --report`
2. **Batch fixing:** `python scripts/linting/repository_linter.py --all-domains --fix`
3. **Export reports:** Add `--save-report` for documentation

## 📊 Error Thresholds

The scripts implement professional error thresholds for incremental quality improvement:

- **Pre-commit hooks:** Allow up to 5 errors per domain (development threshold)
- **Domain linter:** Configurable via `--max-errors` parameter
- **Repository linter:** Reports all issues but doesn't block operations

This approach enables:
- ✅ Incremental quality improvement
- ✅ Non-blocking development workflow
- ✅ Professional quality gates
- ✅ Flexible error tolerance

## 🛠️ Troubleshooting

### Common Issues

**Import errors in Python scripts:**
```bash
# Ensure you're in the documents directory
cd documents

# Check Python path
python -c "import sys; print(sys.path)"
```

**Hook not executing:**
```bash
# Check hook permissions (Unix/Linux)
ls -la .git/hooks/pre-commit

# Make executable if needed
chmod +x .git/hooks/pre-commit
```

**Configuration not found:**
```bash
# Ensure .pymarkdown.json exists in documents directory
ls -la .pymarkdown.json
```

### Getting Help

Each script includes comprehensive help:

```bash
python scripts/linting/domain_linter.py --help
python scripts/linting/repository_linter.py --help
python scripts/git-hooks/setup_git_hooks.py --help
```

## 📝 Legacy Scripts

The following legacy scripts are preserved for compatibility:

- `linting/legacy_autofix.py` - Original markdown autofix
- `linting/fix-*.ps1` - PowerShell-specific fixers
- `cli/lint-docs.bat` - Original batch linting script

**Recommendation:** Use the new professional scripts for all new workflows.

## 🎯 Best Practices

1. **Use domain-specific linting** for focused quality control
2. **Install Git hooks** for automatic quality gates
3. **Generate reports** for documentation and tracking
4. **Configure appropriate thresholds** for your workflow
5. **Run repository-wide analysis** periodically for overview

## 📚 Integration Examples

### CI/CD Integration

```yaml
# Example GitHub Actions workflow
- name: Lint Documentation
  run: |
    cd documents
    python scripts/linting/repository_linter.py --all-domains --max-errors 0
```

### Pre-Push Hook

```bash
#!/bin/sh
# Ensure all domains pass strict linting before push
cd documents
python scripts/linting/repository_linter.py --all-domains --verbose
```

### Automated Reporting

```bash
#!/bin/bash
# Generate weekly quality reports
cd documents
python scripts/linting/repository_linter.py --all-domains --save-report --report
```

---

## 🏆 Quality Status

**Repository Status:** Professional linting infrastructure deployed
**Finance Domain:** ✅ Fully compliant (0 errors)
**All Domains:** ✅ High quality (minimal errors remaining)
**Git Integration:** ✅ Pre-commit hooks available
**Automation Level:** ✅ Fully automated workflow ready
