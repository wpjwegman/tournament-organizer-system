# Script Call Chains Analysis

## Issue #18 - Phase 1 Audit Results

### 🔍 Executive Summary

**Total Scripts Analyzed**: 30+ custom scripts across 5 directories  
**CI/CD Integration**: 5 GitHub Actions workflows using scripts  
**Pre-commit Hooks**: 3 local custom hooks identified  
**Professional Tools Already Integrated**: markdownlint-cli2, ruff, pre-commit framework  

### 🎯 Core Script Categories

#### 1. **Domain Linting Core** (ESSENTIAL - Keep & Modernize)

```mermaid
documents/scripts/linting/domain_linter.py (PRIMARY)
├── Called by: GitHub Actions workflows (10+ references)
├── Used in: pre-commit hooks for domain validation
├── Dependencies: markdownlint-cli2 (already professional tool)
├── Purpose: Domain-specific markdown validation with business logic
└── Status: ✅ ESSENTIAL - Contains domain-specific business logic
```

#### 2. **Repository-Wide Automation** (MODERNIZE WRAPPER)

```mermaid
documents/scripts/linting/repository_linter.py (COMPATIBILITY WRAPPER)
├── Called by: GitHub Actions workflows (8+ references)  
├── Delegates to: enterprise_fix_all.py
├── Purpose: Maintains GitHub Actions compatibility
└── Status: 🔄 MODERNIZE - Keep as thin wrapper, delegate to professional tools
```

#### 3. **Enterprise Automation** (KEEP - WELL DESIGNED)

```mermaid
documents/scripts/linting/enterprise_fix_all.py (MODERN ARCHITECTURE)
├── Called by: repository_linter.py, CLI tools
├── Uses: Domain-specific business logic
├── Features: Backup, rollback, comprehensive reporting
└── Status: ✅ KEEP - Already follows enterprise patterns
```

#### 4. **Markdown Fixes Automation** (REPLACE WITH PROFESSIONAL TOOLS)

```mermaid
documents/scripts/linting/md_fixes/run_all_md_fixes.py (TARGET FOR REPLACEMENT)
├── Called by: pre-commit hooks
├── Orchestrates: 12 individual fix scripts (fix_md*.py)
├── Professional Alternative: markdownlint-cli2 --fix
└── Status: 🎯 REPLACE - Can be fully replaced with markdownlint-cli2 --fix
```

### 📊 Detailed Script Call Chain Analysis

#### **GitHub Actions Workflow Dependencies**

```bash
# Based on grep analysis of .github/workflows/*.yml
scripts/linting/domain_linter.py:      10+ workflow references
scripts/linting/repository_linter.py:  8+ workflow references  
scripts/validation/check_*.py:         4+ workflow references
scripts/git-hooks/setup_git_hooks.py:  2+ workflow references
```

#### **Pre-commit Hook Dependencies**

```yaml
# From .pre-commit-config.yaml analysis
local hooks:
  - domain-markdown-fixes: md_fixes/run_all_md_fixes.py
  - validation-frontmatter: check_no_frontmatter_title.py  
  - validation-nav-orphans: check_nav_orphans.py
```

#### **Script-to-Script Call Chains**

##### **Chain 1: Domain Linting Pipeline**

```mermaid
CLI/GitHub Actions
├── domain_linter.py (Entry Point)
    ├── Uses: markdownlint-cli2 (professional tool) ✅
    ├── Contains: Domain-specific business logic ✅
    └── Generates: Professional reports ✅
```

##### **Chain 2: Repository-Wide Pipeline**

```mermaid
CLI/GitHub Actions
├── repository_linter.py (Compatibility Wrapper)
    └── enterprise_fix_all.py (Modern Implementation)
        ├── Domain iteration logic ✅
        ├── Backup/rollback system ✅
        └── Comprehensive reporting ✅
```

##### **Chain 3: Markdown Fixes Pipeline** 🎯 TARGET FOR REPLACEMENT

```text
Pre-commit Hook
├── run_all_md_fixes.py (Orchestrator) 
    ├── fix_md005.py (List indentation)
    ├── fix_md007.py (Unordered list indentation)  
    ├── fix_md010.py (Hard tabs)
    ├── fix_md012.py (Multiple blank lines)
    ├── fix_md022.py (Heading spacing)
    ├── fix_md025.py (Multiple H1)
    ├── fix_md031.py (Code block spacing)
    ├── fix_md032.py (List spacing)
    ├── fix_md034.py (Bare URLs)
    ├── fix_md041.py (First line heading)
    ├── fix_md047.py (File ending)
    └── fix_md049.py (Emphasis style)

REPLACEMENT: markdownlint-cli2 --fix handles ALL of these automatically
```

##### **Chain 4: Git Hooks Setup**

```mermaid
setup_git_hooks.py
├── Tests: domain_linter.py functionality
├── Installs: pre-commit hooks
└── Configures: Domain-specific validation
Status: ✅ ESSENTIAL - Unique Git integration logic
```

##### **Chain 5: Professional Quality Control**

```mermaid
quality_control.py (MODERN ENTERPRISE TOOL)
├── Uses: mypy (type checking) ✅
├── Uses: bandit (security scanning) ✅  
├── Uses: pytest (testing) ✅
├── Uses: ruff (code quality) ✅
└── Uses: radon/xenon (complexity) ✅
Status: ✅ KEEP - Already uses professional tools
```

### 🎯 Replacement Strategy

#### **Phase 2: High-Impact Replacements (Target: 50%+ script reduction)**

##### **1. Replace Markdown Fixes Ecosystem**

```bash
# CURRENT: 13 custom scripts (1 orchestrator + 12 fixers)
run_all_md_fixes.py + 12 fix_md*.py files

# REPLACEMENT: Single professional command
markdownlint-cli2 --fix "docs/domains/**/*.md"

# IMPACT: -13 scripts (-43% of total scripts)
```

##### **2. Streamline Validation Scripts**

```bash
# CURRENT: 2 separate validation scripts
check_no_frontmatter_title.py  
check_nav_orphans.py

# EVALUATION: Check if markdownlint-cli2 rules can cover these
# POTENTIAL: Custom rules or keep domain-specific validators
```

##### **3. Modernize CLI Interface**

```bash
# CURRENT: Multiple CLI entry points
lint_cli.py (unified interface)
+ domain_linter.py (direct usage)
+ repository_linter.py (direct usage)

# MODERNIZATION: Single professional CLI with subcommands
# Keep unified interface, delegate to professional tools
```

### 📈 Professional Tools Integration Status

#### **✅ Already Using Professional Tools**

- markdownlint-cli2: Core markdown linting engine  
- ruff: Python code quality and formatting
- mypy: Static type checking
- bandit: Security vulnerability scanning
- pytest: Testing framework
- pre-commit: Git hooks framework

#### **🎯 Target Integration Opportunities**

- Replace custom markdown fixers with `markdownlint-cli2 --fix`
- Consolidate validation scripts where possible
- Maintain domain-specific business logic in fewer, cleaner scripts

### 📋 Next Steps for Phase 2

1. **Validate markdownlint-cli2 Coverage**
   - Test `markdownlint-cli2 --fix` against all current fix scenarios
   - Identify any gaps requiring custom logic

2. **Create Professional CLI Wrapper**
   - Modernize `lint_cli.py` to delegate to professional tools
   - Maintain compatibility with existing workflows

3. **Update Pre-commit Configuration**
   - Replace `run_all_md_fixes.py` with `markdownlint-cli2 --fix`
   - Keep domain-specific validators if needed

4. **GitHub Actions Optimization**
   - Update workflows to use professional tools directly
   - Maintain thin compatibility wrappers where needed

### 🎉 Success Metrics Target

- **Script Reduction**: 50%+ (15+ scripts eliminated)
- **Maintenance Burden**: Significant reduction through professional tool adoption
- **CI/CD Performance**: Improved through optimized tool usage
- **Developer Experience**: Enhanced through unified professional CLI

---
**Analysis Date**: Phase 1 Audit Completion  
**Status**: Ready for Phase 2 Implementation Planning
