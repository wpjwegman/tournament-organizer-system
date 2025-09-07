#!/usr/bin/env python3
"""
Enterprise Markdown Automation Suite

Professional, targeted automation for fixing all markdown linting errors
across multiple domains with comprehensive reporting and rollback capability.
"""

import shutil
import subprocess
import sys
import time
from pathlib import Path


class EnterpriseMarkdownFixer:
    def __init__(self, domains: list[str], backup_enabled: bool = True) -> None:
        self.domains = domains
        self.backup_enabled = backup_enabled
        self.backup_dir = Path("markdown_fixes_backup") / f"backup_{int(time.time())}"
        self.fix_results = {}

    def create_backup(self) -> None:
        """Create backup of all files before fixing."""
        if not self.backup_enabled:
            return

        print("🛡️  Creating backup of all markdown files...")
        self.backup_dir.mkdir(parents=True, exist_ok=True)

        for domain in self.domains:
            domain_path = Path(f"documents/docs/domains/{domain}")
            if domain_path.exists():
                backup_domain_path = self.backup_dir / domain
                backup_domain_path.mkdir(parents=True, exist_ok=True)

                for md_file in domain_path.glob("**/*.md"):
                    relative_path = md_file.relative_to(domain_path)
                    backup_file = backup_domain_path / relative_path
                    backup_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(md_file, backup_file)

        print(f"✅ Backup created at: {self.backup_dir}")

    def analyze_errors_before(self) -> dict[str, dict]:
        """Analyze errors before fixing."""
        print("🔍 Analyzing errors before fixing...")
        results = {}

        for domain in self.domains:
            try:
                result = subprocess.run(
                    ["markdownlint-cli2", f"documents/docs/domains/{domain}/**/*.md"],
                    capture_output=True,
                    text=True,
                    check=False,
                )

                error_count = 0
                if result.returncode != 0 and result.stdout:
                    error_count = len([line for line in result.stdout.split("\n") if "MD" in line and ":" in line])

                results[domain] = {"error_count": error_count, "status": "errors" if error_count > 0 else "clean"}

            except Exception as e:
                results[domain] = {"error_count": -1, "status": "error", "message": str(e)}

        return results

    def run_targeted_fixes(self, domain: str) -> dict:
        """Run all fixers on a specific domain."""
        domain_path = Path(f"documents/docs/domains/{domain}")
        if not domain_path.exists():
            return {"status": "error", "message": f"Domain {domain} not found"}

        print(f"🔧 Applying targeted fixes to {domain} domain...")

        # Get all markdown files in the domain
        md_files = list(domain_path.glob("**/*.md"))
        if not md_files:
            return {"status": "no_files", "files_processed": 0}

        files_changed = 0
        fixers_run = 0

        # Run all fixers
        fixer_scripts = [
            "fix_md005.py",
            "fix_md007.py",
            "fix_md010.py",
            "fix_md012.py",
            "fix_md022.py",
            "fix_md025.py",
            "fix_md031.py",
            "fix_md032.py",
            "fix_md034.py",
            "fix_md041.py",
            "fix_md047.py",
            "fix_md049.py",
        ]

        for fixer in fixer_scripts:
            fixer_path = Path(f"scripts/linting/md_fixes/{fixer}")
            if fixer_path.exists():
                try:
                    file_paths = [str(f) for f in md_files]
                    result = subprocess.run(
                        ["uv", "run", "python", str(fixer_path), *file_paths],
                        capture_output=True,
                        text=True,
                        check=False,
                    )

                    if "Fixed" in result.stdout:
                        files_changed += 1
                    fixers_run += 1

                except Exception as e:
                    print(f"  ⚠️  Error running {fixer}: {e}")

        return {
            "status": "completed",
            "files_processed": len(md_files),
            "fixers_run": fixers_run,
            "files_changed": files_changed,
        }

    def analyze_errors_after(self) -> dict[str, dict]:
        """Analyze errors after fixing."""
        print("🔍 Analyzing errors after fixing...")
        return self.analyze_errors_before()  # Same logic

    def run_automation(self) -> dict:
        """Run the complete automation suite."""
        start_time = time.time()

        print("🚀 Starting Enterprise Markdown Automation Suite")
        print("=" * 80)

        # Phase 1: Backup
        if self.backup_enabled:
            self.create_backup()

        # Phase 2: Before analysis
        before_results = self.analyze_errors_before()

        # Phase 3: Apply fixes
        fix_results = {}
        for domain in self.domains:
            fix_results[domain] = self.run_targeted_fixes(domain)

        # Phase 4: After analysis
        after_results = self.analyze_errors_after()

        # Phase 5: Generate report
        execution_time = time.time() - start_time

        return {
            "execution_time": execution_time,
            "backup_location": str(self.backup_dir) if self.backup_enabled else None,
            "before_results": before_results,
            "fix_results": fix_results,
            "after_results": after_results,
        }

    def print_comprehensive_report(self, results: dict) -> None:
        """Print comprehensive automation report."""
        print("\n" + "=" * 80)
        print("📊 ENTERPRISE AUTOMATION RESULTS")
        print("=" * 80)

        # Summary
        total_before = sum(
            r.get("error_count", 0) for r in results["before_results"].values() if r.get("error_count", 0) > 0
        )
        total_after = sum(
            r.get("error_count", 0) for r in results["after_results"].values() if r.get("error_count", 0) > 0
        )
        reduction = total_before - total_after
        reduction_pct = (reduction / total_before * 100) if total_before > 0 else 0

        print(f"⏱️  Execution Time: {results['execution_time']:.2f} seconds")
        print(f"📁 Backup Location: {results['backup_location']}")
        print(f"🎯 Error Reduction: {reduction} errors ({reduction_pct:.1f}% improvement)")

        # Domain details
        print("\n📈 DOMAIN-BY-DOMAIN RESULTS:")
        for domain in self.domains:
            before = results["before_results"].get(domain, {})
            after = results["after_results"].get(domain, {})
            fix_info = results["fix_results"].get(domain, {})

            before_count = before.get("error_count", 0)
            after_count = after.get("error_count", 0)
            files_processed = fix_info.get("files_processed", 0)

            status_emoji = "✅" if after_count == 0 else "⚠️" if after_count < before_count else "❌"

            print(
                f"  {status_emoji} {domain:15s} | {before_count:3d} → {after_count:3d} errors | {files_processed:3d} files processed"
            )

        # Recommendations
        print("\n💡 NEXT STEPS:")
        remaining_domains = [d for d in self.domains if results["after_results"].get(d, {}).get("error_count", 0) > 0]
        if remaining_domains:
            print(f"   Manual review needed for: {', '.join(remaining_domains)}")
            print("   Run: markdownlint-cli2 documents/docs/domains/[domain]/**/*.md")
        else:
            print("   🎉 All domains are now clean! Ready for production.")


def main() -> int:
    domains = [
        "classification",
        "code_of_conduct",
        "communication",
        "discipline",
        "finance",
        "first_aid",
        "foundation",
        "identity",
    ]

    # Parse command line arguments
    selected_domains = domains
    if len(sys.argv) > 1:
        selected_domains = [arg for arg in sys.argv[1:] if arg in domains]
        if not selected_domains:
            print("❌ No valid domains specified. Available domains:")
            print(f"   {', '.join(domains)}")
            return 1

    print(f"🎯 Target domains: {', '.join(selected_domains)}")

    # Run automation
    fixer = EnterpriseMarkdownFixer(selected_domains, backup_enabled=True)
    results = fixer.run_automation()
    fixer.print_comprehensive_report(results)

    return 0


if __name__ == "__main__":
    sys.exit(main())
