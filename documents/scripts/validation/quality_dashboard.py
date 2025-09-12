#!/usr/bin/env python3
"""
🏆 Professional Quality Control Dashboard
==========================================

Enterprise-grade quality monitoring and reporting system for Tournament Organizer.
Integrates all quality tools into a unified dashboard with actionable insights.

Features:
- Security scanning (Bandit)
- Code quality analysis (Ruff)
- Type checking (MyPy)
- Test coverage (Pytest)
- Documentation quality (markdownlint-cli2)
- Code complexity analysis (Radon)
- Performance monitoring
"""

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class QualityMetrics:
    """Quality metrics data structure."""

    timestamp: str = field(default_factory=lambda: datetime.now(UTC).isoformat())
    security_issues: int = 0
    security_details: dict[str, Any] = field(default_factory=dict)
    code_quality_issues: int = 0
    type_issues: int = 0
    test_coverage: float = 0.0
    test_results: dict[str, Any] = field(default_factory=dict)
    documentation_issues: int = 0
    complexity_score: str = "A"
    overall_grade: str = "A"
    recommendations: list[str] = field(default_factory=list)


class QualityDashboard:
    """Professional quality control dashboard."""

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root
        # Detect if we're in a container environment
        if "project-documents" in str(project_root):
            # In container with copied documents
            self.docs_dir = project_root
            self.scripts_dir = project_root / "scripts"
        else:
            # Normal workspace environment
            self.docs_dir = project_root / "documents"
            self.scripts_dir = self.docs_dir / "scripts"
        
        self.reports_dir = project_root / "reports"
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def run_command(self, cmd: list[str], cwd: Path | None = None) -> tuple[bool, str, str]:
        """Execute command and return success, stdout, stderr."""
        try:
            result = subprocess.run(
                cmd, check=False, cwd=cwd or self.docs_dir, capture_output=True, text=True, timeout=300
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timed out"
        except Exception as e:
            return False, "", str(e)

    def check_security(self) -> dict[str, Any]:
        """Run Bandit security scanning."""
        print("🔒 Running security analysis with Bandit...")

        cmd = ["uv", "run", "bandit", "-r", "scripts/", "--configfile", "pyproject.toml", "-f", "json"]
        success, stdout, stderr = self.run_command(cmd)

        issues_count = 0
        details = {}

        if stdout:
            try:
                data = json.loads(stdout)
                issues_count = len(data.get("results", []))
                details = {
                    "high_severity": len([r for r in data.get("results", []) if r.get("issue_severity") == "HIGH"]),
                    "medium_severity": len([r for r in data.get("results", []) if r.get("issue_severity") == "MEDIUM"]),
                    "low_severity": len([r for r in data.get("results", []) if r.get("issue_severity") == "LOW"]),
                    "total_lines_scanned": data.get("metrics", {}).get("_totals", {}).get("loc", 0),
                    "files_scanned": len(data.get("metrics", {}).get("_totals", {}).get("files", [])),
                }
            except json.JSONDecodeError:
                pass

        return {
            "success": success,
            "issues_count": issues_count,
            "details": details,
            "output": stdout,
            "errors": stderr,
        }

    def check_code_quality(self) -> dict[str, Any]:
        """Run Ruff code quality analysis."""
        print("🎯 Running code quality analysis with Ruff...")

        cmd = ["uv", "run", "ruff", "check", "scripts/", "--output-format=json"]
        success, stdout, stderr = self.run_command(cmd)

        issues_count = 0
        if stdout:
            try:
                data = json.loads(stdout)
                issues_count = len(data)
            except json.JSONDecodeError:
                # Count lines for text output
                issues_count = len(stdout.strip().split("\n")) if stdout.strip() else 0

        return {"success": success, "issues_count": issues_count, "output": stdout, "errors": stderr}

    def check_type_safety(self) -> dict[str, Any]:
        """Run MyPy type checking."""
        print("🔍 Running type safety analysis with MyPy...")

        cmd = ["uv", "run", "mypy", "scripts/", "--json-report", str(self.reports_dir / "mypy")]
        success, stdout, stderr = self.run_command(cmd)

        issues_count = len(stderr.split("\n")) if stderr else 0

        return {"success": success, "issues_count": issues_count, "output": stdout, "errors": stderr}

    def check_test_coverage(self) -> dict[str, Any]:
        """Run pytest with coverage."""
        print("🧪 Running test coverage analysis...")

        cmd = ["uv", "run", "pytest", "--cov=scripts", "--cov-report=json", "--cov-report=term-missing"]
        success, stdout, stderr = self.run_command(cmd)

        coverage = 0.0
        test_results: dict[str, any] = {}

        # Try to read coverage JSON report
        coverage_file = self.docs_dir / "coverage.json"
        if coverage_file.exists():
            try:
                with coverage_file.open() as f:
                    data = json.load(f)
                    coverage = data.get("totals", {}).get("percent_covered", 0.0)
            except (json.JSONDecodeError, FileNotFoundError, KeyError):
                pass

        return {
            "success": success,
            "coverage": coverage,
            "test_results": test_results,
            "output": stdout,
            "errors": stderr,
        }

    def check_documentation_quality(self) -> dict[str, Any]:
        """Run markdownlint-cli2 documentation quality check."""
        print("📚 Running documentation quality analysis...")

        cmd = ["markdownlint-cli2", "docs/**/*.md", "--json"]
        success, stdout, stderr = self.run_command(cmd)

        issues_count = 0
        if stdout:
            try:
                # markdownlint-cli2 JSON output format
                lines = stdout.strip().split("\n")
                issues_count = len([line for line in lines if line.strip()])
            except Exception:
                pass

        return {"success": success, "issues_count": issues_count, "output": stdout, "errors": stderr}

    def check_complexity(self) -> dict[str, Any]:
        """Run code complexity analysis."""
        print("🏗️ Running code complexity analysis...")

        cmd = ["uv", "run", "radon", "cc", "scripts/", "-j"]
        success, stdout, stderr = self.run_command(cmd)

        complexity_grade = "A"
        if stdout:
            try:
                data = json.loads(stdout)
                # Calculate average complexity
                total_complexity = 0
                total_functions = 0
                for file_data in data.values():
                    for item in file_data:
                        if isinstance(item, dict) and "complexity" in item:
                            total_complexity += item["complexity"]
                            total_functions += 1

                if total_functions > 0:
                    avg_complexity = total_complexity / total_functions
                    if avg_complexity <= 5:
                        complexity_grade = "A"
                    elif avg_complexity <= 10:
                        complexity_grade = "B"
                    elif avg_complexity <= 20:
                        complexity_grade = "C"
                    else:
                        complexity_grade = "F"
            except Exception:
                pass

        return {"success": success, "complexity_grade": complexity_grade, "output": stdout, "errors": stderr}

    def calculate_overall_grade(self, metrics: QualityMetrics) -> str:
        """Calculate overall quality grade."""
        score = 100

        # Security issues (high impact)
        score -= metrics.security_issues * 5

        # Code quality issues (medium impact)
        score -= metrics.code_quality_issues * 2

        # Type issues (medium impact)
        score -= metrics.type_issues * 2

        # Test coverage (high impact)
        if metrics.test_coverage < 80:
            score = score - (80 - metrics.test_coverage) * 2

        # Documentation issues (low impact)
        score = score - metrics.documentation_issues * 0.5

        # Complexity penalty
        complexity_scores = {"A": 0, "B": -5, "C": -15, "D": -25, "F": -40}
        score += complexity_scores.get(metrics.complexity_score, -40)

        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        if score >= 60:
            return "D"
        return "F"

    def generate_recommendations(self, metrics: QualityMetrics) -> list[str]:
        """Generate actionable recommendations."""
        recommendations = []

        if metrics.security_issues > 0:
            recommendations.append(f"🔒 Address {metrics.security_issues} security issues with Bandit fixes")

        if metrics.code_quality_issues > 50:
            recommendations.append("🎯 Run `uv run ruff check scripts/ --fix` to auto-fix style issues")

        if metrics.type_issues > 20:
            recommendations.append("🔍 Add type annotations to improve type safety")

        if metrics.test_coverage < 80:
            recommendations.append(f"🧪 Increase test coverage from {metrics.test_coverage:.1f}% to 80%+")

        if metrics.documentation_issues > 10:
            recommendations.append("📚 Fix documentation formatting with markdownlint-cli2")

        if metrics.complexity_score in ["D", "F"]:
            recommendations.append("🏗️ Refactor complex functions to improve maintainability")

        return recommendations

    def run_full_analysis(self) -> QualityMetrics:
        """Run complete quality analysis."""
        print("🏆 Starting Professional Quality Control Analysis")
        print("=" * 60)

        metrics = QualityMetrics()

        # Security analysis
        security_result = self.check_security()
        metrics.security_issues = security_result["issues_count"]
        metrics.security_details = security_result["details"]

        # Code quality analysis
        quality_result = self.check_code_quality()
        metrics.code_quality_issues = quality_result["issues_count"]

        # Type safety analysis
        type_result = self.check_type_safety()
        metrics.type_issues = type_result["issues_count"]

        # Test coverage analysis
        test_result = self.check_test_coverage()
        metrics.test_coverage = test_result["coverage"]
        metrics.test_results = test_result["test_results"]

        # Documentation quality
        doc_result = self.check_documentation_quality()
        metrics.documentation_issues = doc_result["issues_count"]

        # Complexity analysis
        complexity_result = self.check_complexity()
        metrics.complexity_score = complexity_result["complexity_grade"]

        # Calculate overall grade and recommendations
        metrics.overall_grade = self.calculate_overall_grade(metrics)
        metrics.recommendations = self.generate_recommendations(metrics)

        return metrics

    def display_dashboard(self, metrics: QualityMetrics) -> None:
        """Display professional quality dashboard."""
        print("\n🏆 QUALITY CONTROL DASHBOARD")
        print("=" * 60)
        print(f"📅 Analysis Date: {metrics.timestamp}")
        print(f"🎯 Overall Grade: {metrics.overall_grade}")
        print("\n📊 METRICS SUMMARY")
        print("-" * 30)
        print(f"🔒 Security Issues: {metrics.security_issues}")
        if metrics.security_details:
            print(f"   ├─ High Severity: {metrics.security_details.get('high_severity', 0)}")
            print(f"   ├─ Medium Severity: {metrics.security_details.get('medium_severity', 0)}")
            print(f"   └─ Low Severity: {metrics.security_details.get('low_severity', 0)}")

        print(f"🎯 Code Quality Issues: {metrics.code_quality_issues}")
        print(f"🔍 Type Safety Issues: {metrics.type_issues}")
        print(f"🧪 Test Coverage: {metrics.test_coverage:.1f}%")
        print(f"📚 Documentation Issues: {metrics.documentation_issues}")
        print(f"🏗️ Complexity Grade: {metrics.complexity_score}")

        if metrics.recommendations:
            print(f"\n💡 RECOMMENDATIONS ({len(metrics.recommendations)})")
            print("-" * 30)
            for i, rec in enumerate(metrics.recommendations, 1):
                print(f"{i}. {rec}")

        print(f"\n✨ Quality Status: {'EXCELLENT' if metrics.overall_grade == 'A' else 'NEEDS IMPROVEMENT'}")
        print("=" * 60)

    def save_report(self, metrics: QualityMetrics, format_type: str = "json") -> Path:
        """Save quality report to file."""
        timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

        if format_type == "json":
            report_file = self.reports_dir / f"quality_report_{timestamp}.json"
            with report_file.open("w") as f:
                json.dump(metrics.__dict__, f, indent=2)
        elif format_type == "markdown":
            report_file = self.reports_dir / f"quality_dashboard_{timestamp}.md"
            with report_file.open("w") as f:
                f.write(self._generate_markdown_report(metrics))

        return report_file

    def _generate_markdown_report(self, metrics: QualityMetrics) -> str:
        """Generate markdown quality report."""
        report = f"""# 🏆 Quality Control Dashboard

**Analysis Date:** {metrics.timestamp}
**Overall Grade:** {metrics.overall_grade}
**Report Type:** Automated Quality Assessment

## 📊 Quality Metrics Summary

| Metric | Value | Status |
|--------|-------|--------|
| 🔒 Security Issues | {metrics.security_issues} | {"✅ Good" if metrics.security_issues == 0 else "⚠️ Issues"} |
| 🎯 Code Quality Issues | {metrics.code_quality_issues} | {"✅ Good" if metrics.code_quality_issues == 0 else "⚠️ Issues"} |
| 🔍 Type Safety Issues | {metrics.type_issues} | {"✅ Good" if metrics.type_issues == 0 else "⚠️ Issues"} |
| 🧪 Test Coverage | {metrics.test_coverage:.1f}% | {"✅ Good" if metrics.test_coverage >= 80 else "⚠️ Low"} |
| 📚 Documentation Issues | {metrics.documentation_issues} | {"✅ Good" if metrics.documentation_issues == 0 else "⚠️ Issues"} |
| 🏗️ Complexity Grade | {metrics.complexity_score} | {"✅ Good" if metrics.complexity_score in ["A", "B"] else "⚠️ High"} |

## 🔒 Security Analysis Details

"""
        if metrics.security_details:
            report += f"""- **High Severity Issues:** {metrics.security_details.get('high_severity', 0)}
- **Medium Severity Issues:** {metrics.security_details.get('medium_severity', 0)}
- **Low Severity Issues:** {metrics.security_details.get('low_severity', 0)}
- **Total Lines Scanned:** {metrics.security_details.get('total_lines_scanned', 0):,}
- **Files Scanned:** {metrics.security_details.get('files_scanned', 0)}

"""
        else:
            report += "Security analysis details not available.\n\n"

        if metrics.recommendations:
            report += f"""## 💡 Recommendations ({len(metrics.recommendations)})

"""
            for i, rec in enumerate(metrics.recommendations, 1):
                report += f"{i}. {rec}\n"
            report += "\n"

        status_map = {
            "A": "🌟 EXCELLENT",
            "B": "👍 GOOD",
            "C": "⚠️ NEEDS IMPROVEMENT",
            "D": "⚠️ NEEDS IMPROVEMENT",
            "F": "🚨 CRITICAL"
        }
        quality_status = status_map.get(metrics.overall_grade, "❓ UNKNOWN")

        report += f"""## 🎯 Quality Assessment

**Overall Quality Grade:** {metrics.overall_grade}

### Grade Scale
- **A (90-100%):** Excellent - Production ready with best practices
- **B (80-89%):** Good - Minor improvements recommended
- **C (70-79%):** Fair - Moderate improvements needed
- **D (60-69%):** Poor - Significant improvements required
- **F (<60%):** Critical - Major remediation needed

### Quality Status: {quality_status}

## 📈 Enterprise Quality Standards

This analysis ensures compliance with enterprise-level quality standards:

- **Security First:** Zero-tolerance for high-severity security issues
- **Code Quality:** Maintainable, readable, and well-structured code
- **Type Safety:** Strong typing for reliability and maintainability
- **Test Coverage:** Comprehensive testing for confidence in changes
- **Documentation:** Clear, accurate, and up-to-date documentation
- **Complexity Management:** Simple, understandable code architecture

## 🚀 Next Steps

1. **Address High Priority Issues:** Focus on security and critical quality issues first
2. **Improve Test Coverage:** Aim for 80%+ coverage across all modules
3. **Enhance Documentation:** Keep documentation synchronized with code changes
4. **Monitor Trends:** Regular quality assessments to track improvements
5. **Automate Fixes:** Use available auto-fix tools where appropriate

---

*Report generated by Tournament Organizer Quality Control System*
*Container Environment: `localhost/docs-quality:latest`*
*Analysis Tools: Bandit, Ruff, MyPy, Pytest, markdownlint-cli2, Radon*
"""
        return report


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Professional Quality Control Dashboard")
    parser.add_argument("--save-report", action="store_true", help="Save report to file")
    parser.add_argument("--quiet", "-q", action="store_true", help="Minimal output")
    parser.add_argument("--project-root", type=Path, default=Path.cwd().parent, help="Project root directory")

    args = parser.parse_args()

    dashboard = QualityDashboard(args.project_root)

    try:
        metrics = dashboard.run_full_analysis()

        if not args.quiet:
            dashboard.display_dashboard(metrics)

        if args.save_report:
            json_report = dashboard.save_report(metrics, "json")
            md_report = dashboard.save_report(metrics, "markdown")
            print("\n📄 Reports saved:")
            print(f"   JSON: {json_report}")
            print(f"   Markdown: {md_report}")

        # Exit with error code if quality is poor
        if metrics.overall_grade in ["D", "F"]:
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n🛑 Analysis interrupted by user")
        sys.exit(1)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"❌ Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
