# 🔄 GitHub Workflow Integration Guide

## Overview

This guide explains how the professional documentation linting scripts are integrated into GitHub workflows to ensure consistent quality control across all documentation in the Tournament Organizer System.

## 🚦 Automated Workflows

### 1. Documentation Quality Control (`documentation-quality.yml`)

**Triggers:**

- Pull requests targeting `main` or `develop` branches
- Pushes to `main` or `develop` branches
- Changes to markdown files or linting configuration

**What it does:**

- ✅ Validates all modified domains with strict linting rules (0 errors allowed)
- ✅ Generates comprehensive reports for repository overview
- ✅ Provides fix suggestions for any issues found
- ✅ Optionally applies automatic fixes when labeled `auto-fix-docs`

**Usage:**
```yaml
# Automatically runs on every PR and push
# Add label "auto-fix-docs" to PR for automatic fixing
```

### 2. Pre-Commit Validation (`pre-commit-validation.yml`)

**Triggers:**

- Pull request events (opened, synchronized, reopened)
- Changes to markdown files

**What it does:**

- ✅ Simulates the same validation as local pre-commit hooks
- ✅ Uses development threshold (5 errors per domain)
- ✅ Generates PR-specific validation reports
- ✅ Provides installation instructions for local hooks

### 3. Automated Quality Reports (`quality-reports.yml`)

**Triggers:**

- Weekly schedule (Mondays at 9:00 AM UTC)
- Manual dispatch with optional auto-fix

**What it does:**

- ✅ Generates comprehensive quality dashboard
- ✅ Creates domain-specific quality scores
- ✅ Optionally applies automatic fixes repository-wide
- ✅ Creates GitHub issues for quality review when needed

## 🎯 Integration Benefits

### For Developers

1. **Immediate Feedback:** Get linting results on every PR
2. **Consistent Standards:** Same rules apply locally and in CI
3. **Auto-Fix Capability:** Automatic resolution of common issues
4. **Clear Guidance:** Specific commands to fix any problems

### For Project Maintainers

1. **Quality Gates:** No low-quality documentation merges to main
2. **Trend Monitoring:** Weekly reports track quality over time
3. **Automated Maintenance:** Regular auto-fixes keep documentation clean
4. **Issue Tracking:** Automatic GitHub issues for quality problems

## 🔧 Local Development Integration

### Install Pre-Commit Hooks

```bash
cd documents
python scripts/git-hooks/setup_git_hooks.py --install
```

### Daily Workflow Commands

```bash
# Check specific domain before committing
python scripts/linting/domain_linter.py finance --check-only

# Fix issues in a domain
python scripts/linting/domain_linter.py finance --fix --auto-stage

# Repository overview
python scripts/linting/repository_linter.py --all-domains --report
```

## 🎭 Workflow Customization

### Error Thresholds

Different thresholds are used for different contexts:

| Context | Threshold | Purpose |
|---------|-----------|---------|
| **Local Pre-commit** | 5 errors/domain | Allow development progress |
| **PR Validation** | 5 errors/domain | Match local experience |
| **Main Branch** | 0 errors/domain | Enforce quality standards |
| **Quality Reports** | Report all | Track trends |

### Customizing Thresholds

Edit the workflow files to adjust error thresholds:

```yaml
# In .github/workflows/documentation-quality.yml
- name: 🎯 Domain-Specific Linting
  run: |
    # Change --max-errors value
    python scripts/linting/domain_linter.py "$DOMAIN" --check-only --max-errors 0
```

### Adding Auto-Fix Labels

To enable automatic fixing in PRs:

1. Add label `auto-fix-docs` to any PR
2. The workflow will automatically apply fixes
3. Commits will be pushed back to the PR branch

## 📊 Quality Monitoring

### Weekly Reports

Every Monday, the system generates:

- Repository-wide quality metrics
- Domain-specific scores
- Trend analysis
- Improvement recommendations

### Dashboard Access

Quality reports are available in:

- GitHub Actions artifacts (90-day retention)
- Automatic GitHub issues (when problems detected)
- Weekly summary comments on main branch

## 🚨 Troubleshooting Workflows

### Common Issues

**Workflow fails with "script not found":**
```bash
# Check script permissions in workflow
chmod +x scripts/cli/domain-lint.sh
chmod +x scripts/git-hooks/*.sh
```

**Linting errors block PR merge:**
```bash
# Local fix process
cd documents
python scripts/linting/domain_linter.py DOMAIN_NAME --fix --auto-stage
git commit -m "Fix linting issues"
git push
```

**Auto-fix not working:**
1. Ensure PR has `auto-fix-docs` label
2. Check workflow permissions in repository settings
3. Verify token has write access

### Debugging Steps

1. **Check workflow logs** in GitHub Actions tab
2. **Download artifacts** for detailed reports
3. **Run scripts locally** to reproduce issues
4. **Check file permissions** for script execution

## 🔄 Continuous Improvement

### Workflow Updates

The workflows automatically stay in sync with script improvements:

- Script path changes are reflected in workflows
- New features are automatically available
- Error handling improvements propagate to CI

### Contributing to Workflows

When updating workflows:

1. Test changes in a fork first
2. Update documentation in this file
3. Verify all paths and commands work
4. Check permissions and token access

## 📚 Best Practices

### For Repository Maintainers

1. **Review quality reports** weekly
2. **Adjust thresholds** based on team needs
3. **Monitor workflow performance** and optimize as needed
4. **Keep scripts updated** with latest improvements

### For Contributors

1. **Install pre-commit hooks** for consistent local experience
2. **Run domain checks** before submitting PRs
3. **Use auto-fix labels** when appropriate
4. **Address linting issues** promptly in PRs

### For Documentation Authors

1. **Check domain status** before major changes
2. **Use fix commands** to resolve issues quickly
3. **Monitor PR validation** results
4. **Follow fix suggestions** provided by workflows

---

## 🎯 Summary

The GitHub workflow integration ensures:

✅ **Consistent Quality:** Same standards locally and in CI  
✅ **Automated Maintenance:** Regular fixes and monitoring  
✅ **Developer Friendly:** Clear guidance and auto-fix options  
✅ **Maintainer Visibility:** Regular reports and issue tracking  

This professional integration provides enterprise-grade documentation quality control while maintaining developer productivity and workflow efficiency.
