#!/usr/bin/env python3
"""
Professional Documentation Linting CLI
======================================

Unified command-line interface for all documentation linting operations.
Provides a clean, professional interface for markdown quality control.

Features:
- Unified interface for all linting operations
- Domain-specific and repository-wide operations
- Git integration and hook management
- Professional help and documentation

Usage:
    python lint_cli.py <command> [options]
    python lint_cli.py domain finance --fix
    python lint_cli.py repository --report
    python lint_cli.py setup-hooks --install
"""

import argparse
import sys
from pathlib import Path

# Add parent directories to path for imports
sys.path.append(str(Path(__file__).parent.parent))

try:
    from linting.domain_linter import DomainLinter
except ImportError:
    # Try alternative import paths
    try:
        sys.path.append(str(Path(__file__).parent.parent / "linting"))
        from domain_linter import DomainLinter
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   Make sure all required modules are available")
        sys.exit(1)


class DocumentationLintCLI:
    """Professional CLI for documentation linting operations."""

    def __init__(self):
        """Initialize the CLI."""
        self.base_path = Path.cwd()

        # Ensure we're in the documents directory
        if self.base_path.name != "documents":
            docs_path = self.base_path / "documents"
            if docs_path.exists():
                self.base_path = docs_path

    def list_available_domains(self) -> list[str]:
        """Get list of available domains.
        
        Returns:
            List of domain names
        """
        domains_path = self.base_path / "docs" / "domains"
        if not domains_path.exists():
            return []

        domains = []
        for item in domains_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                domains.append(item.name)

        return sorted(domains)

    def cmd_domain(self, args) -> int:
        """Handle domain-specific linting command.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code (0 for success, 1 for failure)
        """
        try:
            # Create domain linter
            linter = DomainLinter(args.domain_name, str(self.base_path))

            # Configure options
            fix_mode = args.fix and not args.check_only

            # Run linting
            success = linter.lint_domain(
                fix_mode=fix_mode,
                auto_stage=args.auto_stage,
                max_errors=args.max_errors,
                verbose=args.verbose
            )

            # Generate report if requested
            if args.report or args.save_report:
                report = linter.generate_report(save_to_file=args.save_report)
                if args.report:
                    print("\n" + report)

            return 0 if success else 1

        except Exception as e:
            print(f"❌ Domain linting failed: {e}")
            return 1

    def cmd_repository(self, args) -> int:
        """Handle repository-wide linting command.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code (0 for success, 1 for failure)
        """
        try:
            print("🚀 Running enterprise markdown fixes...")

            # Use our enterprise fixer instead
            from linting.enterprise_fix_all import main as enterprise_main

            # Build arguments for enterprise fixer
            enterprise_args = []
            if args.domains_only:
                # Add specific domains if requested
                domains = self.list_available_domains()
                enterprise_args.extend(domains)

            # Run enterprise fixer
            success = True
            try:
                enterprise_main(enterprise_args if enterprise_args else None)
            except SystemExit as e:
                success = e.code == 0

            return 0 if success else 1

        except Exception as e:
            print(f"❌ Repository linting failed: {e}")
            return 1

    def cmd_setup_hooks(self, args) -> int:
        """Handle Git hooks setup command.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code (0 for success, 1 for failure)
        """
        try:
            if args.install:
                print("🚀 To install Git hooks manually:")
                print("   python scripts/git-hooks/setup_git_hooks.py --install")
            elif args.uninstall:
                print("�️ To uninstall Git hooks manually:")
                print("   python scripts/git-hooks/setup_git_hooks.py --uninstall")
            else:
                print("ℹ️ Git hooks status:")
                print("   Check: python scripts/git-hooks/setup_git_hooks.py --status")

            return 0

        except Exception as e:
            print(f"❌ Git hooks operation failed: {e}")
            return 1

    def cmd_list_domains(self, args) -> int:
        """Handle list domains command.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code (always 0)
        """
        domains = self.list_available_domains()

        if not domains:
            print("ℹ️ No domains found in docs/domains/")
            return 0

        print("📋 Available domains:")
        for domain in domains:
            domain_path = self.base_path / "docs" / "domains" / domain
            md_files = list(domain_path.rglob("*.md"))
            print(f"   {domain} ({len(md_files)} files)")

        return 0


def create_parser() -> argparse.ArgumentParser:
    """Create the main argument parser.
    
    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description="Professional Documentation Linting CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  domain DOMAIN_NAME    Lint a specific domain
  repository           Lint the entire repository
  setup-hooks          Manage Git hooks
  list-domains         List available domains

Examples:
  %(prog)s domain finance --fix --auto-stage
  %(prog)s repository --domains-only
  %(prog)s setup-hooks --install
  %(prog)s list-domains
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Domain command
    domain_parser = subparsers.add_parser("domain", help="Lint a specific domain")
    domain_parser.add_argument("domain_name", help="Domain name to lint")
    domain_parser.add_argument("--fix", action="store_true", help="Apply automatic fixes")
    domain_parser.add_argument("--check-only", action="store_true", help="Only check, don't fix")
    domain_parser.add_argument("--auto-stage", action="store_true", help="Auto-stage fixed files")
    domain_parser.add_argument("--max-errors", type=int, help="Maximum allowed errors")
    domain_parser.add_argument("--report", action="store_true", help="Display detailed report")
    domain_parser.add_argument("--save-report", action="store_true", help="Save report to file")
    domain_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    # Repository command
    repo_parser = subparsers.add_parser("repository", help="Lint the entire repository")
    repo_parser.add_argument("--domains-only", action="store_true", help="Only process domain files")
    repo_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    # Setup hooks command
    hooks_parser = subparsers.add_parser("setup-hooks", help="Manage Git hooks")
    hooks_parser.add_argument("--install", action="store_true", help="Install pre-commit hook")
    hooks_parser.add_argument("--uninstall", action="store_true", help="Uninstall pre-commit hook")
    hooks_parser.add_argument("--force", action="store_true", help="Force installation")

    # List domains command
    subparsers.add_parser("list-domains", help="List available domains")

    return parser


def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Create CLI instance
    cli = DocumentationLintCLI()

    # Dispatch to appropriate command handler
    if args.command == "domain":
        return cli.cmd_domain(args)
    if args.command == "repository":
        return cli.cmd_repository(args)
    if args.command == "setup-hooks":
        return cli.cmd_setup_hooks(args)
    if args.command == "list-domains":
        return cli.cmd_list_domains(args)
    print(f"❌ Unknown command: {args.command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
