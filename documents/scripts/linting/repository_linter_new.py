#!/usr/bin/env python3
"""
Professional Repository-Wide Markdown Linter
============================================

Comprehensive markdown linting tool for entire repositories with detailed reporting,
statistics, and batch processing capabilities.

Features:
- Repository-wide markdown file discovery and processing
- Detailed statistics and error categorization
- Progress tracking for large repositories
- Professional reporting with export capabilities
- Integration with domain-specific linting workflows

Usage:
    python repository_linter.py [options]
    python repository_linter.py --all-domains --report
    python repository_linter.py --fix --verbose --save-report
"""

import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

try:
    from linting.markdown_fixer import MarkdownFixer
except ImportError:
    # Fallback if markdown_fixer is not available
    class MarkdownFixer:
        @staticmethod
        def fix_file(file_path: str) -> bool:
            return False


class RepositoryLinter:
    """Professional repository-wide markdown linter."""
    
    def __init__(self, base_path: Optional[str] = None, verbose: bool = False):
        """Initialize the repository linter.
        
        Args:
            base_path: Base path for the repository (defaults to current directory)
            verbose: Enable verbose output
        """
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.config_path = self.base_path / ".pymarkdown.json"
        self.verbose = verbose
        
        # Statistics tracking
        self.stats = {
            "total_files": 0,
            "files_processed": 0,
            "files_with_errors": 0,
            "total_errors": 0,
            "files_fixed": 0,
            "errors_by_rule": {},
            "errors_by_domain": {},
            "processing_time": 0,
            "start_time": None
        }
        
        # Ensure config exists
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
    
    def discover_markdown_files(self, include_domains_only: bool = False) -> List[Path]:
        """Discover all markdown files in the repository.
        
        Args:
            include_domains_only: If True, only include files in docs/domains
            
        Returns:
            List of markdown file paths
        """
        if include_domains_only:
            domains_path = self.base_path / "docs" / "domains"
            if domains_path.exists():
                return list(domains_path.rglob("*.md"))
            else:
                return []
        else:
            # Find all markdown files, excluding some common directories
            exclude_patterns = {
                ".git", "__pycache__", "node_modules", ".venv", "venv",
                "site", ".mypy_cache", ".pytest_cache"
            }
            
            markdown_files = []
            for md_file in self.base_path.rglob("*.md"):
                # Check if file is in an excluded directory
                if not any(excluded in md_file.parts for excluded in exclude_patterns):
                    markdown_files.append(md_file)
            
            return markdown_files
    
    def get_domain_from_path(self, file_path: Path) -> Optional[str]:
        """Extract domain name from file path.
        
        Args:
            file_path: Path to a markdown file
            
        Returns:
            Domain name if file is in domains directory, None otherwise
        """
        try:
            parts = file_path.relative_to(self.base_path).parts
            if len(parts) >= 3 and parts[0] == "docs" and parts[1] == "domains":
                return parts[2]
        except ValueError:
            pass
        
        return None
    
    def run_pymarkdownlnt_batch(self, files: List[Path]) -> Tuple[bool, Dict[str, List[str]]]:
        """Run pymarkdownlnt on a batch of files.
        
        Args:
            files: List of markdown files to lint
            
        Returns:
            Tuple of (success, errors_by_file)
        """
        if not files:
            return True, {}
        
        # Convert paths to strings relative to base_path
        file_paths = []
        for f in files:
            try:
                file_paths.append(str(f.relative_to(self.base_path)))
            except ValueError:
                file_paths.append(str(f))
        
        try:
            result = subprocess.run([
                "uv", "run", "pymarkdownlnt",
                "--config", str(self.config_path),
                "scan"
            ] + file_paths,
            cwd=self.base_path,
            capture_output=True,
            text=True,
            timeout=600  # 10 minute timeout
            )
            
            # Parse output for errors
            errors_by_file = {}
            if result.stdout:
                for line in result.stdout.split('\n'):
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Check if line contains file path and error
                    if '.md:' in line and ':' in line:
                        try:
                            # Parse format: file.md:line:col: ERROR_CODE: Message
                            parts = line.split(':', 3)
                            if len(parts) >= 4:
                                file_part = parts[0]
                                if file_part.endswith('.md'):
                                    error_detail = ':'.join(parts[1:])
                                    
                                    if file_part not in errors_by_file:
                                        errors_by_file[file_part] = []
                                    errors_by_file[file_part].append(error_detail)
                        except Exception:
                            continue
            
            return result.returncode == 0, errors_by_file
            
        except subprocess.TimeoutExpired:
            return False, {"timeout": ["Linting process timed out"]}
        except Exception as e:
            return False, {"error": [f"Failed to run pymarkdownlnt: {e}"]}
    
    def apply_fixes_batch(self, files: List[Path]) -> int:
        """Apply automatic fixes to a batch of files.
        
        Args:
            files: List of files to fix
            
        Returns:
            Number of files successfully fixed
        """
        fixed_count = 0
        
        for file_path in files:
            try:
                if MarkdownFixer.fix_file(str(file_path)):
                    fixed_count += 1
                    if self.verbose:
                        relative_path = file_path.relative_to(self.base_path)
                        print(f"  ✅ Fixed: {relative_path}")
            except Exception as e:
                if self.verbose:
                    relative_path = file_path.relative_to(self.base_path)
                    print(f"  ❌ Failed to fix {relative_path}: {e}")
        
        return fixed_count
    
    def update_statistics(self, files: List[Path], errors_by_file: Dict[str, List[str]]):
        """Update internal statistics based on linting results.
        
        Args:
            files: List of files that were processed
            errors_by_file: Dictionary of errors by file
        """
        self.stats["files_processed"] += len(files)
        
        for file_path in files:
            file_str = str(file_path.relative_to(self.base_path))
            
            if file_str in errors_by_file:
                self.stats["files_with_errors"] += 1
                file_errors = errors_by_file[file_str]
                self.stats["total_errors"] += len(file_errors)
                
                # Track errors by rule
                for error in file_errors:
                    if ": MD" in error:
                        try:
                            rule_code = error.split(": ")[1].split(":")[0]
                            self.stats["errors_by_rule"][rule_code] = \
                                self.stats["errors_by_rule"].get(rule_code, 0) + 1
                        except Exception:
                            pass
                
                # Track errors by domain
                domain = self.get_domain_from_path(file_path)
                if domain:
                    self.stats["errors_by_domain"][domain] = \
                        self.stats["errors_by_domain"].get(domain, 0) + len(file_errors)
    
    def generate_comprehensive_report(self) -> str:
        """Generate a comprehensive repository linting report.
        
        Returns:
            Formatted report as string
        """
        report = f"""
# Repository-Wide Markdown Linting Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Repository Path:** `{self.base_path}`
**Processing Time:** {self.stats['processing_time']:.2f} seconds

## Summary Statistics

- **Total Files Found:** {self.stats['total_files']}
- **Files Processed:** {self.stats['files_processed']}
- **Files with Errors:** {self.stats['files_with_errors']}
- **Total Errors:** {self.stats['total_errors']}
- **Files Fixed:** {self.stats['files_fixed']}

## Error Analysis

### By Rule Type
"""
        
        if self.stats['errors_by_rule']:
            for rule, count in sorted(self.stats['errors_by_rule'].items()):
                report += f"- **{rule}:** {count} occurrences\n"
        else:
            report += "✅ No errors found!\n"
        
        report += "\n### By Domain\n"
        
        if self.stats['errors_by_domain']:
            for domain, count in sorted(self.stats['errors_by_domain'].items()):
                report += f"- **{domain}:** {count} errors\n"
        else:
            report += "✅ No domain-specific errors!\n"
        
        # Overall status
        report += "\n## Overall Status\n"
        
        if self.stats['total_errors'] == 0:
            report += "🎉 **PERFECT** - Repository is fully compliant!\n"
        elif self.stats['total_errors'] <= 10:
            report += "✅ **EXCELLENT** - Only minor issues remain\n"
        elif self.stats['total_errors'] <= 50:
            report += "⚠️ **GOOD** - Some issues need attention\n"
        else:
            report += "❌ **NEEDS WORK** - Multiple issues require fixing\n"
        
        return report
    
    def save_report(self, report_content: str, output_file: Optional[Path] = None) -> Path:
        """Save report to file.
        
        Args:
            report_content: Report content to save
            output_file: Output file path (defaults to timestamped file)
            
        Returns:
            Path to saved report file
        """
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.base_path / f"repository_lint_report_{timestamp}.md"
        
        output_file.write_text(report_content, encoding='utf-8')
        return output_file
    
    def lint_repository(self, 
                       domains_only: bool = False,
                       fix_mode: bool = False,
                       batch_size: int = 50) -> bool:
        """Main repository linting function.
        
        Args:
            domains_only: Only process files in docs/domains
            fix_mode: Apply automatic fixes
            batch_size: Number of files to process in each batch
            
        Returns:
            True if no errors found, False otherwise
        """
        self.stats["start_time"] = time.time()
        
        # Discover files
        print("🔍 Discovering markdown files...")
        files = self.discover_markdown_files(include_domains_only=domains_only)
        self.stats["total_files"] = len(files)
        
        if not files:
            print("ℹ️ No markdown files found")
            return True
        
        scope = "domains" if domains_only else "repository"
        print(f"📁 Found {len(files)} markdown files in {scope}")
        
        # Process files in batches
        all_errors = {}
        
        for i in range(0, len(files), batch_size):
            batch = files[i:i + batch_size]
            batch_num = (i // batch_size) + 1
            total_batches = (len(files) + batch_size - 1) // batch_size
            
            if self.verbose:
                print(f"📦 Processing batch {batch_num}/{total_batches} ({len(batch)} files)...")
            
            # Apply fixes first if in fix mode
            if fix_mode:
                fixed_count = self.apply_fixes_batch(batch)
                self.stats["files_fixed"] += fixed_count
                
                if self.verbose and fixed_count > 0:
                    print(f"   🔧 Fixed {fixed_count} files in batch")
            
            # Run linting
            success, batch_errors = self.run_pymarkdownlnt_batch(batch)
            all_errors.update(batch_errors)
            
            # Update statistics
            self.update_statistics(batch, batch_errors)
            
            if self.verbose:
                batch_error_count = sum(len(errors) for errors in batch_errors.values())
                print(f"   📊 Batch {batch_num}: {batch_error_count} errors")
        
        # Calculate final processing time
        self.stats["processing_time"] = time.time() - self.stats["start_time"]
        
        return self.stats["total_errors"] == 0


def main():
    """Main entry point for the repository linter."""
    parser = argparse.ArgumentParser(
        description="Professional repository-wide markdown linter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --all-domains --report
  %(prog)s --fix --verbose --save-report
  %(prog)s --domains-only --fix
        """
    )
    
    parser.add_argument("--all-domains", "--domains-only", action="store_true",
                       help="Only process files in docs/domains directory")
    parser.add_argument("--fix", action="store_true",
                       help="Apply automatic fixes to files")
    parser.add_argument("--report", action="store_true",
                       help="Display comprehensive report")
    parser.add_argument("--save-report", action="store_true",
                       help="Save report to file")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Enable verbose output")
    parser.add_argument("--batch-size", type=int, default=50,
                       help="Number of files to process in each batch")
    parser.add_argument("--base-path", 
                       help="Base path for repository (default: current directory)")
    
    args = parser.parse_args()
    
    try:
        # Create linter instance
        linter = RepositoryLinter(args.base_path, args.verbose)
        
        print("🚀 Starting repository-wide markdown linting...")
        
        # Run linting
        success = linter.lint_repository(
            domains_only=args.all_domains,
            fix_mode=args.fix,
            batch_size=args.batch_size
        )
        
        # Display summary
        print(f"\n📊 Processing completed in {linter.stats['processing_time']:.2f}s")
        print(f"   Files processed: {linter.stats['files_processed']}")
        print(f"   Files with errors: {linter.stats['files_with_errors']}")
        print(f"   Total errors: {linter.stats['total_errors']}")
        
        if args.fix:
            print(f"   Files fixed: {linter.stats['files_fixed']}")
        
        # Generate and display report
        if args.report or args.save_report:
            report = linter.generate_comprehensive_report()
            
            if args.report:
                print(report)
            
            if args.save_report:
                report_file = linter.save_report(report)
                print(f"\n📄 Report saved to: {report_file}")
        
        # Exit with appropriate code
        sys.exit(0 if success else 1)
        
    except FileNotFoundError as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
