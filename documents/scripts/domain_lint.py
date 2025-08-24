#!/usr/bin/env python3
"""
Per-Domain Markdown Linting Tool

Professional solution for domain-specific markdown linting with Git integration.
Perfect for incremental documentation quality improvements.

Features:
- Domain-specific linting and fixing
- Git pre-commit integration
- Configurable error thresholds
- Detailed reporting per domain
- Automatic staging of fixes

Usage:
    python scripts/domain_lint.py <domain_name> [options]
    python scripts/domain_lint.py finance --fix --auto-stage
    python scripts/domain_lint.py finance --check-only --report
"""
from __future__ import annotations

import argparse
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import time


class DomainLinter:
    def __init__(self, domain: str, base_path: Path, config_path: Path, verbose: bool = False):
        self.domain = domain
        self.base_path = base_path
        self.config_path = config_path
        self.verbose = verbose
        self.domain_path = base_path / "docs" / "domains" / domain
        
        if not self.domain_path.exists():
            raise ValueError(f"Domain '{domain}' not found at {self.domain_path}")
    
    def get_domain_files(self) -> List[Path]:
        """Get all markdown files in the domain."""
        return list(self.domain_path.glob("**/*.md"))
    
    def run_lint_check(self) -> Tuple[bool, Dict[str, List[str]]]:
        """Run pymarkdownlnt with proper configuration on domain files."""
        if self.verbose:
            print(f"🔍 Linting {self.domain} domain...")
        
        try:
            result = subprocess.run([
                "uv", "run", "pymarkdownlnt", 
                "--config", str(self.config_path),
                "scan", str(self.domain_path), "--recurse"
            ], 
            capture_output=True, 
            text=True, 
            cwd=self.base_path
            )
            
            if result.returncode == 0:
                return True, {}
            
            # Parse errors
            errors = {}
            if result.stdout.strip():
                for line in result.stdout.strip().split('\n'):
                    if line.strip():
                        if '.md:' in line:
                            # Extract file path and error
                            parts = line.split('.md:', 1)
                            if len(parts) == 2:
                                file_path = parts[0] + '.md'
                                error_detail = parts[1]
                                
                                if file_path not in errors:
                                    errors[file_path] = []
                                errors[file_path].append(error_detail.strip())
            
            return False, errors
            
        except Exception as e:
            return False, {"error": [f"Failed to run linter: {e}"]}
    
    def apply_fixes(self) -> Tuple[int, int]:
        """Apply automatic fixes to domain files."""
        if self.verbose:
            print(f"🔧 Applying fixes to {self.domain} domain...")
        
        files = self.get_domain_files()
        fixed_count = 0
        fix_script = self.base_path / "scripts" / "fix_markdown_lint.py"
        
        for file_path in files:
            try:
                result = subprocess.run([
                    "python", str(fix_script), str(file_path)
                ], 
                capture_output=True, 
                text=True,
                cwd=self.base_path
                )
                
                if "Fixed:" in result.stdout:
                    fixed_count += 1
                    if self.verbose:
                        print(f"  ✅ Fixed: {file_path.name}")
                        
            except Exception as e:
                if self.verbose:
                    print(f"  ❌ Error fixing {file_path.name}: {e}")
        
        return fixed_count, len(files)
    
    def stage_changes(self) -> bool:
        """Stage the fixed files in Git."""
        try:
            result = subprocess.run([
                "git", "add", str(self.domain_path)
            ], 
            capture_output=True, 
            text=True,
            cwd=self.base_path
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def generate_report(self, errors: Dict[str, List[str]]) -> str:
        """Generate a domain-specific error report."""
        if not errors:
            return f"✅ {self.domain.title()} domain: No linting errors found!"
        
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
        
        report = f"📊 {self.domain.title()} Domain Linting Report\n"
        report += "=" * 50 + "\n"
        report += f"❌ Found {total_errors} errors in {len(errors)} files\n\n"
        
        if error_types:
            report += "Error Summary:\n"
            for error_type, count in sorted(error_types.items()):
                report += f"  {error_type}: {count} occurrences\n"
        
        return report
    
    def save_report(self, errors: Dict[str, List[str]], output_file: Optional[Path] = None) -> Path:
        """Save detailed report to file."""
        if output_file is None:
            output_file = self.base_path / f"lint_report_{self.domain}.md"
        
        report = self.generate_report(errors)
        
        if errors:
            report += "\n\nDetailed Errors:\n"
            for file_path, file_errors in errors.items():
                if file_errors and any(e.strip() for e in file_errors):
                    relative_path = Path(file_path).relative_to(self.base_path)
                    report += f"\n### `{relative_path}`\n"
                    for error in file_errors:
                        if error.strip():
                            report += f"- {error}\n"
        
        output_file.write_text(report, encoding="utf-8")
        return output_file


def main():
    parser = argparse.ArgumentParser(
        description="Per-Domain Markdown Linting Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python scripts/domain_lint.py finance --check-only
    python scripts/domain_lint.py finance --fix --auto-stage
    python scripts/domain_lint.py tournament --fix --report --verbose
    python scripts/domain_lint.py identity --check-only --save-report
        """
    )
    
    parser.add_argument("domain", help="Domain name to lint (e.g., finance, tournament)")
    parser.add_argument("--check-only", action="store_true", 
                       help="Run lint check without fixing")
    parser.add_argument("--fix", action="store_true",
                       help="Apply automatic fixes")
    parser.add_argument("--auto-stage", action="store_true",
                       help="Automatically stage fixed files in Git")
    parser.add_argument("--report", action="store_true",
                       help="Display detailed report")
    parser.add_argument("--save-report", action="store_true",
                       help="Save report to file")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Detailed output")
    parser.add_argument("--threshold", type=int, default=0,
                       help="Maximum acceptable errors (default: 0)")
    
    args = parser.parse_args()
    
    # Setup paths
    script_path = Path(__file__).parent
    base_path = script_path.parent
    config_path = base_path / ".pymarkdown.json"
    
    if not config_path.exists():
        print(f"❌ Configuration file not found: {config_path}")
        return 1
    
    try:
        # Initialize domain linter
        linter = DomainLinter(args.domain, base_path, config_path, args.verbose)
        
        print(f"🎯 Processing {args.domain} domain...")
        files = linter.get_domain_files()
        print(f"📁 Found {len(files)} markdown files")
        
        # Run initial check
        start_time = time.time()
        passed, errors = linter.run_lint_check()
        check_time = time.time() - start_time
        
        if args.verbose:
            print(f"✅ Lint check completed in {check_time:.2f}s")
        
        # Generate and display report
        if args.report or not passed:
            report = linter.generate_report(errors)
            print(f"\n{report}")
        
        # Save report if requested
        if args.save_report:
            report_file = linter.save_report(errors)
            print(f"📄 Report saved to: {report_file}")
        
        # Check threshold
        total_errors = sum(len(file_errors) for file_errors in errors.values())
        if total_errors > args.threshold:
            print(f"⚠️  Error count ({total_errors}) exceeds threshold ({args.threshold})")
            
            if not args.fix:
                print("💡 Use --fix to apply automatic fixes")
                return 1
        
        # Apply fixes if requested and needed
        if args.fix and not passed:
            print(f"\n🔧 Applying automatic fixes to {args.domain} domain...")
            fix_start = time.time()
            fixed_count, total_count = linter.apply_fixes()
            fix_time = time.time() - fix_start
            
            print(f"✅ Applied fixes to {fixed_count}/{total_count} files in {fix_time:.2f}s")
            
            # Auto-stage if requested
            if args.auto_stage and fixed_count > 0:
                if linter.stage_changes():
                    print(f"📝 Staged changes for {args.domain} domain")
                else:
                    print("⚠️  Failed to stage changes")
            
            # Run final verification
            print("\n🔍 Running final verification...")
            final_passed, final_errors = linter.run_lint_check()
            
            if final_passed:
                print(f"🎉 {args.domain.title()} domain now passes all linting checks!")
                return 0
            else:
                final_report = linter.generate_report(final_errors)
                print(f"\n{final_report}")
                print("\n💡 Some issues require manual fixes")
                return 1
        
        return 0 if passed else 1
        
    except ValueError as e:
        print(f"❌ {e}")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
