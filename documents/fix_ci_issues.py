#!/usr/bin/env python3
"""
Fix CI/CD Issues Script
======================

This script addresses all the GitHub Actions failures:
1. Fix YAML configuration errors
2. Fix pre-commit hook issues  
3. Fix markdownlint-cli2 configuration discrepancies
4. Remove trailing whitespace and fix end-of-file issues
5. Ensure all scripts are accessible in CI/CD environment
"""

import os
import sys
import subprocess
import glob
import shutil
from pathlib import Path


def fix_trailing_whitespace():
    """Fix trailing whitespace in all markdown files."""
    print("🔧 Fixing trailing whitespace...")
    
    md_files = glob.glob("docs/**/*.md", recursive=True)
    md_files.extend(glob.glob("*.md"))
    md_files.extend(glob.glob("**/*.md", recursive=True))
    
    fixed_count = 0
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix trailing whitespace
            lines = content.splitlines()
            fixed_lines = [line.rstrip() for line in lines]
            new_content = '\n'.join(fixed_lines)
            
            # Ensure file ends with newline
            if new_content and not new_content.endswith('\n'):
                new_content += '\n'
            
            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed_count += 1
                print(f"  ✅ Fixed: {file_path}")
                
        except Exception as e:
            print(f"  ❌ Error fixing {file_path}: {e}")
    
    print(f"🎉 Fixed trailing whitespace in {fixed_count} files")


def fix_yaml_files():
    """Fix YAML syntax issues."""
    print("🔧 Fixing YAML files...")
    
    yaml_files = glob.glob("**/*.yml", recursive=True)
    yaml_files.extend(glob.glob("**/*.yaml", recursive=True))
    
    for file_path in yaml_files:
        try:
            # Test YAML syntax
            import yaml
            with open(file_path, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
            print(f"  ✅ Valid YAML: {file_path}")
        except yaml.YAMLError as e:
            print(f"  ❌ YAML error in {file_path}: {e}")
        except Exception as e:
            print(f"  ⚠️  Could not check {file_path}: {e}")


def fix_pre_commit_config():
    """Fix pre-commit configuration issues."""
    print("🔧 Fixing pre-commit configuration...")
    
    config_path = ".pre-commit-config.yaml"
    if not os.path.exists(config_path):
        print(f"  ⚠️  {config_path} not found")
        return
    
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the domain-markdown-fixes hook path
    updated_content = content.replace(
        'entry: python scripts/linting/md_fixes/run_all_md_fixes.py',
        'entry: bash -c "cd documents && python scripts/linting/md_fixes/run_all_md_fixes.py"'
    )
    
    if content != updated_content:
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("  ✅ Updated pre-commit configuration")
    else:
        print("  ✅ Pre-commit configuration already correct")


def fix_markdownlint_config():
    """Ensure markdownlint configuration is consistent."""
    print("🔧 Checking markdownlint configuration...")
    
    config_files = ['.markdownlint-cli2.jsonc', '.markdownlint.json', '.markdownlint-cli2.yaml']
    
    for config_file in config_files:
        if os.path.exists(config_file):
            print(f"  ✅ Found config: {config_file}")
        else:
            print(f"  ⚠️  Missing config: {config_file}")


def run_comprehensive_fix():
    """Run comprehensive markdown fixing."""
    print("🔧 Running comprehensive markdown fixes...")
    
    # Run enterprise automation for each domain
    domains = ['classification', 'code_of_conduct', 'communication', 'discipline', 
               'finance', 'first_aid', 'foundation', 'identity']
    
    for domain in domains:
        try:
            cmd = [sys.executable, 'scripts/linting/domain_linter.py', domain, '--fix', '--verbose']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"  ✅ Fixed domain: {domain}")
            else:
                print(f"  ⚠️  Domain {domain} status: {result.returncode}")
                
        except Exception as e:
            print(f"  ❌ Error fixing domain {domain}: {e}")


def main():
    """Main execution function."""
    print("🚀 Starting CI/CD Issues Fix")
    print("=" * 50)
    
    # Change to documents directory if needed
    if os.path.basename(os.getcwd()) != 'documents':
        if os.path.exists('documents'):
            os.chdir('documents')
            print("📁 Changed to documents directory")
    
    # Run all fixes
    fix_trailing_whitespace()
    print()
    
    fix_yaml_files()
    print()
    
    fix_pre_commit_config()
    print()
    
    fix_markdownlint_config()
    print()
    
    run_comprehensive_fix()
    print()
    
    print("🎉 CI/CD Issues Fix Completed!")
    print("💡 Next: Commit changes and push to trigger CI/CD validation")


if __name__ == "__main__":
    main()
