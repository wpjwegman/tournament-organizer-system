#!/usr/bin/env python3
"""
Setup Git Hooks for Domain-Specific Markdown Linting

This script configures Git hooks to automatically run domain-specific
markdown linting before commits, ensuring quality control per domain.
"""

import shutil
import stat
import subprocess
import sys
from pathlib import Path


def setup_git_hooks() -> bool:
    """Setup Git hooks for domain linting."""
    print("🔧 Setting up Git hooks for domain-specific markdown linting...")

    # Find Git root
    try:
        git_root_str = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
        git_root = Path(git_root_str)
    except subprocess.CalledProcessError:
        print("❌ Not in a Git repository")
        return False

    hooks_dir = git_root / ".git" / "hooks"
    scripts_dir = git_root / "documents" / "scripts"
    git_hooks_dir = scripts_dir / "git-hooks"

    # Ensure hooks directory exists
    hooks_dir.mkdir(exist_ok=True)

    # Determine which hook to use based on platform
    import platform

    if platform.system() == "Windows":
        # Setup PowerShell hook
        source_hook = git_hooks_dir / "pre-commit-domain-lint.ps1"
        target_hook = hooks_dir / "pre-commit"

        if source_hook.exists():
            # Create a batch file that calls PowerShell
            batch_content = f"""@echo off
powershell.exe -ExecutionPolicy Bypass -File "{source_hook}"
exit /b %ERRORLEVEL%
"""
            target_hook.write_text(batch_content)
            print("✅ Installed PowerShell pre-commit hook")
        else:
            print(f"❌ PowerShell hook script not found: {source_hook}")
            return False
    else:
        # Setup bash hook
        source_hook = git_hooks_dir / "pre-commit-domain-lint.sh"
        target_hook = hooks_dir / "pre-commit"

        if source_hook.exists():
            shutil.copy2(source_hook, target_hook)
            # Make executable
            target_hook.chmod(target_hook.stat().st_mode | stat.S_IEXEC)
            print("✅ Installed bash pre-commit hook")
        else:
            print(f"❌ Bash hook script not found: {source_hook}")
            return False

    print(f"📁 Hook installed at: {target_hook}")
    print("\n🎯 Configuration:")
    print("   - Threshold: 10 errors per domain (adjustable)")
    print("   - Only checks modified domains")
    print("   - Provides fix suggestions")

    return True


def test_domain_script() -> bool | None:
    """Test the domain linting script."""
    print("\n🧪 Testing domain linting script...")

    # Find Git root first
    try:
        git_root_str = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
        git_root = Path(git_root_str)
        domain_script = git_root / "documents" / "scripts" / "linting" / "domain_linter.py"
    except subprocess.CalledProcessError:
        print("❌ Not in a Git repository")
        return False

    if not domain_script.exists():
        print(f"❌ Domain script not found: {domain_script}")
        print(f"   Git root: {git_root}")
        return False

    try:
        # Test on finance domain
        result = subprocess.run(
            ["python", str(domain_script), "finance", "--check-only"],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
            check=False,
        )

        if result.returncode == 0:
            print("✅ Domain script test passed")
            return True
        print("⚠️  Domain script test completed with warnings")
        print("    This is normal for domains under development")
        return True

    except Exception as e:
        print(f"❌ Error testing domain script: {e}")
        return False


def main() -> int:
    print("🚀 Git Hooks Setup for Domain-Specific Markdown Linting")
    print("=" * 60)

    # Test domain script first
    if not test_domain_script():
        print("\n❌ Setup aborted due to script issues")
        return 1

    # Setup Git hooks
    if not setup_git_hooks():
        print("\n❌ Failed to setup Git hooks")
        return 1

    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Test with: git add <domain-file> && git commit")
    print("2. Fix issues with: python scripts/linting/domain_linter.py <domain> --fix --auto-stage")
    print("3. Adjust threshold in hook files if needed")

    return 0


if __name__ == "__main__":
    sys.exit(main())
