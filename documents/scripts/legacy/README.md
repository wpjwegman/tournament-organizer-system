# Archive Directory

## Replaced Scripts - Issue #18 Phase 2

This directory contains scripts that have been replaced with professional tools during the scripts modernization initiative.

### Purpose

- **Backup**: Preserve original scripts for rollback capability
- **Documentation**: Maintain history of what was replaced and why
- **Reference**: Enable comparison with professional tool implementations

### Replacement Summary

#### Markdown Fixes Ecosystem (Archived in Phase 2B)

**Replaced Scripts**: 13 custom scripts → `markdownlint-cli2 --fix`

- `run_all_md_fixes.py` (orchestrator)
- 12 individual `fix_md*.py` scripts

**Professional Replacement**: `markdownlint-cli2 --fix "docs/domains/**/*.md"`

**Benefits**:

- ✅ Professional tool support and maintenance
- ✅ Same functionality with better performance
- ✅ Reduced custom code maintenance burden
- ✅ Industry-standard markdown formatting

### Restoration Instructions

If rollback is needed:

1. Move scripts from `archive/` back to their original locations
2. Update `.pre-commit-config.yaml` to use archived scripts
3. Update GitHub Actions workflows to reference archived scripts
4. Test functionality thoroughly

### Scripts Modernization Status

- **Phase 1**: ✅ Audit completed (30+ scripts analyzed)
- **Phase 2**: 🚀 Implementation in progress (50%+ reduction target)
- **Target**: Professional tool adoption while preserving essential business logic

---
**Archive Date**: August 2025  
**Issue**: #18 Scripts Analysis and Modernization  
**Phase**: 2B - Core Replacement
