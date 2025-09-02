#!/usr/bin/env python3
"""
🚀 Quality Control Quick Start
=============================

Easy commands for running quality checks and automated fixes.
Perfect for daily development workflow.

Usage:
    python quick_quality.py check          # Run all quality checks
    python quick_quality.py fix            # Auto-fix issues
    python quick_quality.py dashboard      # Show quality dashboard
    python quick_quality.py security       # Security analysis only
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run command with user feedback."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed (exit code: {e.returncode})")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python quick_quality.py [check|fix|dashboard|security]")
        sys.exit(1)

    action = sys.argv[1]
    project_root = Path(__file__).parent.parent.parent.parent

    print(f"🎯 Quality Control - {action.upper()}")
    print("=" * 40)

    if action == "check":
        print("Running comprehensive quality checks...")
        run_command("uv run bandit -r scripts/", "Security scan")
        run_command("uv run ruff check scripts/", "Code quality")
        run_command("uv run mypy scripts/", "Type checking")
        run_command("markdownlint-cli2 docs/**/*.md", "Documentation")
        run_command("uv run python scripts/validation/quality_dashboard.py", "Quality dashboard")

    elif action == "fix":
        print("Running automated fixes...")
        run_command("uv run python scripts/validation/ci_issue_resolver.py --commit", "Automated fixes")

    elif action == "dashboard":
        print("Showing quality dashboard...")
        run_command("uv run python scripts/validation/quality_dashboard.py", "Quality dashboard")

    elif action == "security":
        print("Running security analysis...")
        run_command("uv run bandit -r scripts/ -f text", "Security analysis")

    else:
        print(f"Unknown action: {action}")
        print("Available actions: check, fix, dashboard, security")
        sys.exit(1)


if __name__ == "__main__":
    main()
