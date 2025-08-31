"""
Test configuration and shared fixtures for the tournament organizer documentation system.
"""
import pytest
from pathlib import Path
from unittest.mock import Mock, patch
import tempfile
import shutil


@pytest.fixture
def temp_docs_structure():
    """Create a temporary documentation structure for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create test structure
        docs_path = temp_path / "docs" / "domains"
        docs_path.mkdir(parents=True)
        
        # Create sample domain
        finance_path = docs_path / "finance"
        finance_path.mkdir()
        
        # Create sample markdown files
        (finance_path / "README.md").write_text("""# Finance Domain

## Overview

This is a test finance domain.

### Features

- Budget management
- Expense tracking

## Implementation

More details here.
""", encoding="utf-8")
        
        (finance_path / "budget.md").write_text("""# Budget Management

## Planning

Budget planning details.

### Categories

- Revenue
- Expenses
""", encoding="utf-8")
        
        yield temp_path


@pytest.fixture
def mock_subprocess():
    """Mock subprocess for testing without executing external commands."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = Mock(
            returncode=0,
            stdout="",
            stderr=""
        )
        yield mock_run


@pytest.fixture
def mock_pathlib():
    """Mock pathlib operations for testing."""
    with patch("pathlib.Path") as mock_path:
        yield mock_path


@pytest.fixture
def sample_markdown_content():
    """Sample markdown content for testing."""
    return {
        "valid": """---
title: "Test Document" 
---

# Test Document

This is a valid markdown document.

## Section 1

Content here.

## Section 2

More content.
""",
        "invalid": """# Multiple H1 Headers

## Section

# Another H1 - This should be flagged

Content with issues:

-  Inconsistent list indentation
  - Mixed indentation
 - More issues


""",
        "with_errors": """# Test Document



## Section with too many blank lines

Content with tabs:	tab character here

- List item
  - Subitem with wrong indentation
""",
    }
