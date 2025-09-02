"""
Unit tests for the domain linter functionality.

Tests cover:
- Domain validation
- File discovery
- Linting operations
- Error reporting
- Fix application
"""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import Mock
from unittest.mock import patch

import pytest

# Add the parent directory to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from scripts.linting.domain_linter import DomainLinter
except ImportError as e:
    pytest.skip(f"Could not import DomainLinter: {e}", allow_module_level=True)


class TestDomainLinter:
    """Test suite for DomainLinter class."""

    def test_init_valid_domain(self, temp_docs_structure) -> None:
        """Test initialization with a valid domain."""
        base_path = temp_docs_structure
        domain = "finance"

        linter = DomainLinter(domain, base_path)

        assert linter.domain == domain
        assert linter.base_path == base_path
        assert linter.domain_path == base_path / "docs" / "domains" / domain

    def test_init_invalid_domain(self, temp_docs_structure) -> None:
        """Test initialization with an invalid domain raises ValueError."""
        base_path = temp_docs_structure
        invalid_domain = "nonexistent"

        with pytest.raises(ValueError, match="Domain 'nonexistent' not found"):
            DomainLinter(invalid_domain, base_path)

    def test_get_domain_files(self, temp_docs_structure) -> None:
        """Test discovery of markdown files in domain."""
        base_path = temp_docs_structure
        domain = "finance"

        linter = DomainLinter(domain, base_path)
        files = linter.get_domain_files()

        # Should find the two .md files we created
        assert len(files) == 2
        assert all(f.suffix == ".md" for f in files)
        assert any(f.name == "README.md" for f in files)
        assert any(f.name == "budget.md" for f in files)

    @patch("subprocess.run")
    def test_run_lint_check_success(self, mock_run, temp_docs_structure) -> None:
        """Test successful lint check with no errors."""
        mock_run.return_value = Mock(returncode=0, stdout="")

        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        passed, errors = linter.run_lint_check()

        assert passed is True
        assert errors == {}

    @patch("subprocess.run")
    def test_run_lint_check_with_errors(self, mock_run, temp_docs_structure) -> None:
        """Test lint check that finds errors."""
        # Mock markdownlint-cli2 output with errors
        mock_output = """docs/domains/finance/README.md:1:1: MD041 First line in a file should be a top-level heading
docs/domains/finance/budget.md:5:1: MD022 Headings should be surrounded by blank lines"""

        mock_run.return_value = Mock(returncode=1, stdout=mock_output)

        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        passed, errors = linter.run_lint_check()

        assert passed is False
        assert len(errors) == 2
        assert "docs/domains/finance/README.md" in errors
        assert "docs/domains/finance/budget.md" in errors

    @patch("subprocess.run")
    def test_apply_fixes(self, mock_run, temp_docs_structure) -> None:
        """Test application of automatic fixes."""
        # Mock successful fix operations
        mock_run.return_value = Mock(returncode=0, stdout="Fixed issues")

        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        # Create mock fix scripts
        fix_scripts_dir = base_path / "scripts" / "linting" / "md_fixes"
        fix_scripts_dir.mkdir(parents=True)
        (fix_scripts_dir / "fix_md022.py").touch()
        (fix_scripts_dir / "fix_md031.py").touch()

        fixed_count, total_count = linter.apply_fixes()

        # Should attempt to run markdownlint-cli2 --fix and custom fixers
        assert mock_run.call_count >= 1
        assert isinstance(fixed_count, int)
        assert isinstance(total_count, int)

    def test_generate_report_no_errors(self, temp_docs_structure) -> None:
        """Test report generation when no errors found."""
        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        report = linter.generate_report({})

        assert "Finance domain: No linting errors found!" in report
        assert "✅" in report

    def test_generate_report_with_errors(self, temp_docs_structure) -> None:
        """Test report generation with errors."""
        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        errors = {
            "file1.md": ["Line 1: MD041 First line should be heading"],
            "file2.md": ["Line 5: MD022 Headings need blank lines"],
        }

        report = linter.generate_report(errors)

        assert "Finance Domain Linting Report" in report
        assert "Found 2 errors in 2 files" in report
        assert "MD041" in report
        assert "MD022" in report

    def test_save_report(self, temp_docs_structure) -> None:
        """Test saving report to file."""
        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        # Use relative paths from base_path for realistic error simulation
        errors = {str(base_path / "docs" / "domains" / "finance" / "file1.md"): ["Line 1: MD041 Error"]}
        output_file = base_path / "test_report.md"

        saved_file = linter.save_report(errors, output_file)

        assert saved_file == output_file
        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        assert "Finance Domain Linting Report" in content
        assert "file1.md" in content

    @patch("subprocess.run")
    def test_stage_changes_success(self, mock_run, temp_docs_structure) -> None:
        """Test successful Git staging of changes."""
        mock_run.return_value = Mock(returncode=0)

        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        result = linter.stage_changes()

        assert result is True
        mock_run.assert_called_once()

    @patch("subprocess.run")
    def test_stage_changes_failure(self, mock_run, temp_docs_structure) -> None:
        """Test Git staging failure."""
        mock_run.return_value = Mock(returncode=1)

        base_path = temp_docs_structure
        domain = "finance"
        linter = DomainLinter(domain, base_path)

        result = linter.stage_changes()

        assert result is False


class TestDomainLinterIntegration:
    """Integration tests for domain linter."""

    @pytest.mark.integration
    def test_full_workflow(self, temp_docs_structure) -> None:
        """Test complete linting workflow."""
        base_path = temp_docs_structure
        domain = "finance"

        # Create linter
        linter = DomainLinter(domain, base_path)

        # Verify domain setup
        files = linter.get_domain_files()
        assert len(files) > 0

        # Mock linting to avoid external dependencies
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="")

            # Run lint check
            passed, errors = linter.run_lint_check()

            # Verify behavior
            assert isinstance(passed, bool)
            assert isinstance(errors, dict)


@pytest.mark.unit
class TestDomainLinterUtils:
    """Test utility functions and edge cases."""

    def test_domain_linter_with_custom_config(self, temp_docs_structure) -> None:
        """Test domain linter with custom configuration path."""
        base_path = temp_docs_structure
        domain = "finance"
        custom_config = base_path / "custom.json"
        custom_config.write_text("{}", encoding="utf-8")

        linter = DomainLinter(domain, base_path, custom_config)

        assert linter.config_path == custom_config

    def test_domain_linter_verbose_mode(self, temp_docs_structure) -> None:
        """Test domain linter in verbose mode."""
        base_path = temp_docs_structure
        domain = "finance"

        linter = DomainLinter(domain, base_path, verbose=True)

        assert linter.verbose is True

    def test_empty_domain_directory(self, temp_docs_structure) -> None:
        """Test behavior with empty domain directory."""
        base_path = temp_docs_structure

        # Create empty domain
        empty_domain = "empty"
        empty_path = base_path / "docs" / "domains" / empty_domain
        empty_path.mkdir()

        linter = DomainLinter(empty_domain, base_path)
        files = linter.get_domain_files()

        assert len(files) == 0
