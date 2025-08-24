#!/usr/bin/env python3
"""
Comprehensive Markdown Documentation Linter and Fixer

This script provides professional-grade markdown linting and fixing for the entire
documentation repository. It handles the configuration issues and provides detailed
reporting.

Features:
- Proper configuration file usage
- Comprehensive error reporting
- Batch processing with progress tracking
- Pre/post validation
- Detailed statistics

Usage:
    python scripts/comprehensive_markdown_lint.py [options]

Options:
    --check-only        Run lint check without fixing
    --domain DOMAIN     Process specific domain only (e.g., finance)
    --all-domains      Process all domain files
    --all-files        Process ALL markdown files in repository
    --fix              Apply automatic fixes
    --verbose          Detailed output
"""
from __future__ import annotations

import argparse
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple
import time


class MarkdownLinter:
    def __init__(self, config_path: Path, verbose: bool = False):
        self.config_path = config_path
        self.verbose = verbose
        self.base_path = config_path.parent
        
    def run_lint_check(self, paths: List[Path]) -> Tuple[bool, Dict[str, List[str]]]:
        """Run pymarkdownlnt with proper configuration and return results."""
        errors = {}
        all_passed = True
        
        for path in paths:
            if self.verbose:
                print(f"Checking {path}...")
            
            try:
                result = subprocess.run([
                    "uv", "run", "pymarkdownlnt", 
                    "--config", str(self.config_path),
                    "scan", str(path)
                ], 
                capture_output=True, 
                text=True, 
                cwd=self.base_path
                )
                
                if result.returncode != 0:
                    all_passed = False
                    errors[str(path)] = result.stdout.strip().split('\n') if result.stdout.strip() else []
                    
            except Exception as e:
                all_passed = False
                errors[str(path)] = [f"Error running linter: {e}"]
                
        return all_passed, errors
    
    def apply_fixes(self, paths: List[Path]) -> Tuple[int, int]:
        """Apply automatic fixes using the fix script."""
        fixed_count = 0
        total_count = len(paths)
        
        fix_script = self.base_path / "scripts" / "fix_markdown_lint.py"
        
        for path in paths:
            if self.verbose:
                print(f"Fixing {path}...")
            
            try:
                result = subprocess.run([
                    "python", str(fix_script), str(path)
                ], 
                capture_output=True, 
                text=True,
                cwd=self.base_path
                )
                
                if "Fixed:" in result.stdout:
                    fixed_count += 1
                    
            except Exception as e:
                print(f"Error fixing {path}: {e}")
                
        return fixed_count, total_count
    
    def generate_report(self, errors: Dict[str, List[str]]) -> str:
        """Generate a comprehensive error report."""
        if not errors:
            return "✅ No linting errors found!"
        
        error_types = {}
        total_errors = 0
        
        for file_path, file_errors in errors.items():
            for error in file_errors:
                if error.strip():
                    total_errors += 1
                    # Extract error type (e.g., MD013, MD032)
                    if ": MD" in error:
                        error_type = error.split(": ")[1].split(":")[0]
                        error_types[error_type] = error_types.get(error_type, 0) + 1
        
        report = f"❌ Found {total_errors} linting errors in {len(errors)} files\n\n"
        report += "Error Summary:\n"
        for error_type, count in sorted(error_types.items()):
            report += f"  {error_type}: {count} occurrences\n"
        
        report += "\nDetailed Errors:\n"
        for file_path, file_errors in errors.items():
            if file_errors and any(e.strip() for e in file_errors):
                report += f"\n📄 {file_path}:\n"
                for error in file_errors:
                    if error.strip():
                        report += f"  {error}\n"
        
        return report


def get_markdown_files(base_path: Path, pattern: str) -> List[Path]:
    """Get markdown files based on pattern."""
    if pattern == "all":
        return list(base_path.rglob("*.md"))
    elif pattern == "domains":
        return list((base_path / "docs" / "domains").rglob("*.md"))
    elif pattern.startswith("domain:"):
        domain = pattern.split(":", 1)[1]
        return list((base_path / "docs" / "domains" / domain).glob("*.md"))
    else:
        # Treat as glob pattern
        return list(base_path.glob(pattern))


def main():
    parser = argparse.ArgumentParser(
        description="Comprehensive Markdown Documentation Linter and Fixer",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--check-only", action="store_true", 
                       help="Run lint check without fixing")
    parser.add_argument("--domain", type=str, 
                       help="Process specific domain only (e.g., finance)")
    parser.add_argument("--all-domains", action="store_true",
                       help="Process all domain files")
    parser.add_argument("--all-files", action="store_true",
                       help="Process ALL markdown files in repository")
    parser.add_argument("--fix", action="store_true",
                       help="Apply automatic fixes")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Detailed output")
    
    args = parser.parse_args()
    
    # Determine base path and config
    script_path = Path(__file__).parent
    base_path = script_path.parent
    config_path = base_path / ".pymarkdown.json"
    
    if not config_path.exists():
        print(f"❌ Configuration file not found: {config_path}")
        return 1
    
    # Determine file pattern
    if args.all_files:
        pattern = "all"
        scope = "entire repository"
    elif args.all_domains:
        pattern = "domains"
        scope = "all domains"
    elif args.domain:
        pattern = f"domain:{args.domain}"
        scope = f"{args.domain} domain"
    else:
        pattern = "docs/domains/finance/*.md"
        scope = "finance domain (default)"
    
    print(f"🔍 Processing {scope}...")
    
    # Get files to process
    files = get_markdown_files(base_path, pattern)
    
    if not files:
        print(f"❌ No markdown files found for pattern: {pattern}")
        return 1
    
    print(f"📁 Found {len(files)} markdown files")
    
    # Initialize linter
    linter = MarkdownLinter(config_path, args.verbose)
    
    # Run initial check
    print("\n🔍 Running initial lint check...")
    start_time = time.time()
    passed, errors = linter.run_lint_check(files)
    check_time = time.time() - start_time
    
    print(f"✅ Initial check completed in {check_time:.2f}s")
    
    if passed:
        print("🎉 All files pass linting!")
        return 0
    
    # Generate and display report
    report = linter.generate_report(errors)
    print("\n" + "="*60)
    print("LINTING REPORT")
    print("="*60)
    print(report)
    
    # Apply fixes if requested
    if args.fix and not args.check_only:
        print("\n🔧 Applying automatic fixes...")
        fix_start = time.time()
        fixed_count, total_count = linter.apply_fixes(files)
        fix_time = time.time() - fix_start
        
        print(f"✅ Applied fixes to {fixed_count}/{total_count} files in {fix_time:.2f}s")
        
        # Run final check
        print("\n🔍 Running final verification...")
        final_passed, final_errors = linter.run_lint_check(files)
        
        if final_passed:
            print("🎉 All files now pass linting!")
            return 0
        else:
            final_report = linter.generate_report(final_errors)
            print("\n" + "="*60)
            print("REMAINING ISSUES (require manual fixes)")
            print("="*60)
            print(final_report)
            return 1
    
    elif args.check_only:
        print("\n💡 Run with --fix to apply automatic fixes")
        return 1
    
    else:
        print("\n💡 Use --fix to apply automatic fixes, or --check-only to just report")
        return 0


if __name__ == "__main__":
    sys.exit(main())
