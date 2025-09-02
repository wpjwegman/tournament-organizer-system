#!/usr/bin/env python3
"""
⚡ Automated CI Issue Resolution System
=====================================

Intelligent automation for common CI/CD failures with GitHub Actions integration.
Automatically detects, analyzes, and fixes common issues to reduce manual intervention.

Features:
- Automatic markdown linting fixes
- Code formatting corrections
- Import organization
- Security issue triaging
- Pull request auto-fixes
"""

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FixResult:
    """Result of an automated fix attempt."""

    success: bool
    description: str
    files_modified: list[str]
    details: str


class CIIssueResolver:
    """Automated CI issue resolution system."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.docs_dir = project_root / "documents"
        self.scripts_dir = self.docs_dir / "scripts"

    def run_command(self, cmd: list[str], cwd: Path | None = None) -> tuple[bool, str, str]:
        """Execute command and return success, stdout, stderr."""
        try:
            result = subprocess.run(
                cmd, check=False, cwd=cwd or self.docs_dir, capture_output=True, text=True, timeout=300
            )
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)

    def fix_markdown_issues(self) -> FixResult:
        """Automatically fix markdown linting issues."""
        print("📚 Auto-fixing markdown issues...")

        # Run markdownlint-cli2 with --fix flag
        cmd = ["markdownlint-cli2", "--fix", "docs/**/*.md"]
        success, stdout, stderr = self.run_command(cmd)

        # Check which files were modified
        git_cmd = ["git", "diff", "--name-only"]
        _, git_stdout, _ = self.run_command(git_cmd, self.project_root)
        modified_files = [f for f in git_stdout.strip().split("\n") if f.endswith(".md")]

        return FixResult(
            success=success,
            description="Fixed markdown formatting issues",
            files_modified=modified_files,
            details=f"Processed markdown files with markdownlint-cli2. {len(modified_files)} files modified.",
        )

    def fix_python_formatting(self) -> FixResult:
        """Automatically fix Python code formatting."""
        print("🐍 Auto-fixing Python formatting...")

        # Run Ruff with --fix flag
        cmd = ["uv", "run", "ruff", "check", "scripts/", "--fix"]
        success, stdout, stderr = self.run_command(cmd)

        # Run Ruff format
        format_cmd = ["uv", "run", "ruff", "format", "scripts/"]
        format_success, format_stdout, format_stderr = self.run_command(format_cmd)

        # Check which files were modified
        git_cmd = ["git", "diff", "--name-only"]
        _, git_stdout, _ = self.run_command(git_cmd, self.project_root)
        modified_files = [f for f in git_stdout.strip().split("\n") if f.endswith(".py")]

        return FixResult(
            success=success and format_success,
            description="Fixed Python code formatting and style",
            files_modified=modified_files,
            details=f"Applied Ruff fixes and formatting. {len(modified_files)} Python files modified.",
        )

    def fix_import_organization(self) -> FixResult:
        """Organize Python imports."""
        print("📦 Organizing Python imports...")

        # Ruff handles import sorting via isort rules
        cmd = ["uv", "run", "ruff", "check", "scripts/", "--select=I", "--fix"]
        success, stdout, stderr = self.run_command(cmd)

        git_cmd = ["git", "diff", "--name-only"]
        _, git_stdout, _ = self.run_command(git_cmd, self.project_root)
        modified_files = [f for f in git_stdout.strip().split("\n") if f.endswith(".py")]

        return FixResult(
            success=success,
            description="Organized Python imports",
            files_modified=modified_files,
            details=f"Sorted and organized imports in {len(modified_files)} files.",
        )

    def analyze_security_issues(self) -> FixResult:
        """Analyze and triage security issues."""
        print("🔒 Analyzing security issues...")

        cmd = ["uv", "run", "bandit", "-r", "scripts/", "-f", "json"]
        success, stdout, stderr = self.run_command(cmd)

        issues_analysis = {"total": 0, "high": 0, "medium": 0, "low": 0, "fixable": 0}

        if stdout:
            try:
                data = json.loads(stdout)
                results = data.get("results", [])
                issues_analysis["total"] = len(results)

                for issue in results:
                    severity = issue.get("issue_severity", "").upper()
                    if severity == "HIGH":
                        issues_analysis["high"] += 1
                    elif severity == "MEDIUM":
                        issues_analysis["medium"] += 1
                    elif severity == "LOW":
                        issues_analysis["low"] += 1

                    # Check if issue is auto-fixable
                    test_id = issue.get("test_id", "")
                    if test_id in ["B101", "B601", "B602"]:  # Common auto-fixable issues
                        issues_analysis["fixable"] += 1

            except json.JSONDecodeError:
                pass

        return FixResult(
            success=True,
            description="Security analysis completed",
            files_modified=[],
            details=f"Found {issues_analysis['total']} security issues: "
            f"{issues_analysis['high']} high, {issues_analysis['medium']} medium, "
            f"{issues_analysis['low']} low severity. {issues_analysis['fixable']} auto-fixable.",
        )

    def fix_pre_commit_issues(self) -> FixResult:
        """Fix common pre-commit hook failures."""
        print("🔧 Fixing pre-commit issues...")

        # Run pre-commit with auto-fix
        cmd = ["uv", "run", "pre-commit", "run", "--all-files"]
        success, stdout, stderr = self.run_command(cmd)

        # Check for modified files
        git_cmd = ["git", "diff", "--name-only"]
        _, git_stdout, _ = self.run_command(git_cmd, self.project_root)
        modified_files = git_stdout.strip().split("\n") if git_stdout.strip() else []

        return FixResult(
            success=True,  # Pre-commit often "fails" while fixing issues
            description="Ran pre-commit hooks with auto-fixes",
            files_modified=modified_files,
            details=f"Pre-commit hooks processed and fixed issues in {len(modified_files)} files.",
        )

    def create_auto_fix_commit(self, fixes: list[FixResult]) -> bool:
        """Create a commit with all automated fixes."""
        if not any(fix.files_modified for fix in fixes):
            print("No files were modified - skipping commit")
            return True

        print("📝 Creating automated fix commit...")

        # Stage all modified files
        add_cmd = ["git", "add", "."]
        success, _, _ = self.run_command(add_cmd, self.project_root)

        if not success:
            return False

        # Create commit message
        commit_msg = "🤖 Automated CI issue fixes\n\n"
        for fix in fixes:
            if fix.files_modified:
                commit_msg += f"- {fix.description} ({len(fix.files_modified)} files)\n"

        commit_msg += "\nGenerated by CI issue resolver"

        # Commit changes
        commit_cmd = ["git", "commit", "-m", commit_msg]
        success, _, _ = self.run_command(commit_cmd, self.project_root)

        return success

    def run_auto_fixes(self, create_commit: bool = False) -> list[FixResult]:
        """Run all automated fixes."""
        print("⚡ Starting Automated CI Issue Resolution")
        print("=" * 50)

        fixes = []

        # Run each fix type
        fixes.append(self.fix_markdown_issues())
        fixes.append(self.fix_python_formatting())
        fixes.append(self.fix_import_organization())
        fixes.append(self.analyze_security_issues())
        fixes.append(self.fix_pre_commit_issues())

        # Display results
        print("\n📊 FIX RESULTS SUMMARY")
        print("-" * 30)

        total_files_modified = set()
        for fix in fixes:
            status = "✅" if fix.success else "❌"
            print(f"{status} {fix.description}")
            print(f"   Files modified: {len(fix.files_modified)}")
            print(f"   Details: {fix.details}")
            total_files_modified.update(fix.files_modified)
            print()

        print(f"🎯 Total unique files modified: {len(total_files_modified)}")

        # Create commit if requested
        if create_commit and total_files_modified:
            if self.create_auto_fix_commit(fixes):
                print("✅ Automated fix commit created successfully")
            else:
                print("❌ Failed to create automated fix commit")

        return fixes

    def generate_github_comment(self, fixes: list[FixResult]) -> str:
        """Generate GitHub PR comment with fix summary."""
        comment = "## 🤖 Automated CI Issue Resolution\n\n"
        comment += "The following issues have been automatically analyzed and fixed:\n\n"

        for fix in fixes:
            status = "✅" if fix.success else "❌"
            comment += f"- {status} **{fix.description}**\n"
            if fix.files_modified:
                comment += f"  - Modified {len(fix.files_modified)} files\n"
            comment += f"  - {fix.details}\n\n"

        total_files = len(set(f for fix in fixes for f in fix.files_modified))
        if total_files > 0:
            comment += f"**Total**: {total_files} files were automatically fixed.\n\n"
            comment += "Please review the changes and re-run the CI pipeline.\n"
        else:
            comment += "No automatic fixes were applied. Manual review may be required.\n"

        comment += "\n---\n*Generated by Tournament Organizer CI automation*"
        return comment


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Automated CI Issue Resolution")
    parser.add_argument("--commit", action="store_true", help="Create commit with fixes")
    parser.add_argument("--github-comment", action="store_true", help="Generate GitHub comment")
    parser.add_argument("--project-root", type=Path, default=Path.cwd().parent, help="Project root")

    args = parser.parse_args()

    resolver = CIIssueResolver(args.project_root)

    try:
        fixes = resolver.run_auto_fixes(create_commit=args.commit)

        if args.github_comment:
            comment = resolver.generate_github_comment(fixes)
            print("\n" + "=" * 50)
            print("GITHUB PR COMMENT")
            print("=" * 50)
            print(comment)

        # Exit with success if all critical fixes succeeded
        critical_fixes = [f for f in fixes if f.description.startswith(("Fixed markdown", "Fixed Python"))]
        if all(f.success for f in critical_fixes):
            sys.exit(0)
        else:
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n🛑 Automated fixes interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error during automated fixes: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
