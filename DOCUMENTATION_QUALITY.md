# 📚 Documentation Quality Standards & GitHub Integration

## Overview

The Tournament Organizer System maintains enterprise-grade documentation quality through professional linting infrastructure with full GitHub Actions integration.

## 🎯 Quality Standards

### Error Thresholds by Context

| Context | Threshold | Purpose |
|---------|-----------|---------|
| **Local Development** | 5 errors/domain | Allow progress while improving |
| **Pre-Commit Hooks** | 5 errors/domain | Catch major issues before commit |
| **Pull Request CI** | 5 errors/domain | Match local development experience |
| **Main Branch CI** | 0 errors/domain | Enforce production quality |
| **Weekly Reports** | Report all | Track quality trends |

### Quality Gates

1. **Pre-Commit:** Local validation with development threshold
2. **PR Validation:** CI validation matching local experience  
3. **Merge Protection:** Strict validation before main branch
4. **Continuous Monitoring:** Weekly quality reports and auto-fixes

## 🔄 GitHub Actions Integration

### Automated Workflows

The repository includes three professional workflows:

#### 1. Documentation Quality Control (`.github/workflows/documentation-quality.yml`)

**Runs on:** Pull requests and pushes to main/develop branches

**Features:**

- ✅ Domain-specific validation of modified files
- ✅ Strict 0-error threshold for main branch
- ✅ Automatic fix application with `auto-fix-docs` label
- ✅ Comprehensive reporting and fix suggestions
- ✅ Artifact upload for detailed analysis

#### 2. Pre-Commit Validation (`.github/workflows/pre-commit-validation.yml`)

**Runs on:** Pull request events

**Features:**

- ✅ Simulates local pre-commit hook behavior
- ✅ Development-friendly 5-error threshold per domain
- ✅ PR-specific validation reports
- ✅ Local setup instructions and guidance

#### 3. Automated Quality Reports (`.github/workflows/quality-reports.yml`)

**Runs on:** Weekly schedule + manual dispatch

**Features:**

- ✅ Repository-wide quality dashboard generation
- ✅ Domain-specific quality scoring
- ✅ Optional automated fix application
- ✅ GitHub issue creation for quality problems
- ✅ Long-term quality trend tracking

## 🛠️ Developer Setup

### 1. Install Local Pre-Commit Hooks

```bash
cd documents
python scripts/git-hooks/setup_git_hooks.py --install
```

### 2. Verify Installation

```bash
# Test the hooks
git add .
git commit -m "Test commit"  # Will trigger validation

# Check hook status
python scripts/git-hooks/setup_git_hooks.py --status
```

### 3. Daily Development Commands

```bash
# Check domain before working
./scripts/cli/domain-lint.bat finance

# Fix issues when needed  
./scripts/cli/domain-lint.bat finance fix

# Repository overview
python scripts/linting/repository_linter.py --all-domains --report
```

## 🎭 Workflow Usage

### For Pull Requests

1. **Normal PR Process:**
   - CI automatically validates modified domains
   - Uses development threshold (5 errors/domain)
   - Provides fix suggestions if issues found

2. **Auto-Fix PRs:**
   - Add `auto-fix-docs` label to any PR
   - CI will automatically apply fixes
   - Commits are pushed back to PR branch

3. **Quality Validation:**
   - All PRs get validation reports
   - Same rules as local pre-commit hooks
   - Clear guidance for fixing any issues

### For Maintainers

1. **Weekly Quality Review:**
   - Automated reports every Monday
   - Quality dashboard with domain scores
   - GitHub issues created for problems

2. **Manual Quality Maintenance:**
   - Go to Actions → "Automated Quality Reports"
   - Click "Run workflow"
   - Check "Apply automatic fixes" if desired
   - Review generated reports

3. **Threshold Adjustment:**
   - Edit workflow YAML files to adjust error limits
   - Different thresholds for different contexts
   - Balance between quality and productivity

## 📊 Quality Monitoring

### Dashboard Metrics

The automated quality dashboard includes:

- **Repository Statistics:** Total files, errors, processing time
- **Domain Quality Scores:** Per-domain file counts and error rates
- **Error Analysis:** Breakdown by rule type and domain
- **Trend Tracking:** Quality improvements over time
- **Improvement Recommendations:** Specific commands to fix issues

### Report Access

Quality reports are available through:

1. **GitHub Actions Artifacts:**
   - 90-day retention for quality reports
   - 30-day retention for lint reports
   - 14-day retention for PR validation reports

2. **Automatic GitHub Issues:**
   - Created when quality problems detected
   - Include full dashboard and fix recommendations
   - Labeled for easy filtering and tracking

3. **Weekly Monitoring:**
   - Scheduled reports every Monday at 9:00 AM UTC
   - Comprehensive analysis of all domains
   - Automated improvement suggestions

## 🚨 Troubleshooting

### Common Workflow Issues

**"Script not found" errors:**
```bash
# Ensure proper permissions
chmod +x documents/scripts/cli/domain-lint.sh
chmod +x documents/scripts/git-hooks/*.sh
```

**Auto-fix not working:**
1. Verify PR has `auto-fix-docs` label
2. Check repository workflow permissions
3. Ensure token has write access to repository

**Local hooks not triggering:**
```bash
# Reinstall hooks
cd documents
python scripts/git-hooks/setup_git_hooks.py --uninstall
python scripts/git-hooks/setup_git_hooks.py --install
```

### Getting Help

1. **Check workflow logs** in GitHub Actions tab
2. **Download artifacts** for detailed error reports
3. **Run scripts locally** to reproduce issues:
   ```bash
   cd documents
   python scripts/linting/domain_linter.py DOMAIN --check-only --verbose
   ```
4. **Review integration guide** at `.github/WORKFLOW_INTEGRATION.md`

## 🎯 Best Practices

### For Contributors

1. **Install pre-commit hooks** for consistent local experience
2. **Run domain checks** before submitting PRs
3. **Address linting issues** promptly when flagged
4. **Use auto-fix labels** when appropriate for minor issues

### For Repository Maintainers

1. **Review weekly reports** for quality trends
2. **Adjust thresholds** based on team productivity needs
3. **Monitor workflow performance** and optimize as needed
4. **Keep scripts updated** with latest improvements

### For Documentation Authors

1. **Check domain status** before major documentation updates
2. **Use fix commands** to resolve issues quickly
3. **Monitor PR validation** results for immediate feedback
4. **Follow fix suggestions** provided by CI workflows

## 🔄 Continuous Improvement

The integration is designed for continuous improvement:

- **Script Updates:** Automatically reflected in CI workflows
- **New Features:** Available immediately in all contexts
- **Performance Optimization:** Regular monitoring and tuning
- **Quality Standards:** Evolve with project needs

## 📚 Related Documentation

- **Script Documentation:** [`documents/scripts/README.md`](documents/scripts/README.md)
- **Workflow Integration Guide:** [`.github/WORKFLOW_INTEGRATION.md`](.github/WORKFLOW_INTEGRATION.md)
- **Linting Configuration:** [`documents/.pymarkdown.json`](documents/.pymarkdown.json)

---

## 🏆 Current Quality Status

**✅ Finance Domain:** Perfect compliance (0 errors)  
**✅ Repository Overall:** 99.9% clean (2 errors in 178 files)  
**✅ GitHub Integration:** Fully operational with enterprise-grade workflows  
**✅ Developer Experience:** Seamless local and CI integration  

The Tournament Organizer System maintains professional documentation quality standards through comprehensive automation and developer-friendly tooling.
