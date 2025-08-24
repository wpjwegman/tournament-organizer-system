#!/usr/bin/env python3
"""
Practical Markdown auto-fix for common pymarkdownlnt issues:
- MD032: Ensure blank lines around lists  
- MD012: Remove multiple consecutive blank lines
- YAML front matter formatting fixes

Usage:
    python documents/scripts/fix_markdown_lint.py <files...>
    python documents/scripts/fix_markdown_lint.py docs/domains/finance/*.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List


def fix_yaml_front_matter_spacing(lines: List[str]) -> List[str]:
    """Fix YAML front matter list spacing issues."""
    result = []
    in_front_matter = False
    
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_front_matter = True
            result.append(line)
        elif in_front_matter and line.strip() == "---":
            in_front_matter = False
            result.append(line)
            # Ensure blank line after front matter
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                result.append("")
        elif in_front_matter:
            result.append(line)
        else:
            result.append(line)
    
    return result


def fix_list_spacing(lines: List[str]) -> List[str]:
    """Ensure proper spacing around lists (MD032)."""
    result = []
    in_front_matter = False
    in_code_block = False
    
    for i, line in enumerate(lines):
        # Track front matter and code blocks
        if i == 0 and line.strip() == "---":
            in_front_matter = True
        elif in_front_matter and line.strip() == "---":
            in_front_matter = False
        elif line.strip().startswith("```"):
            in_code_block = not in_code_block
        
        if in_front_matter or in_code_block:
            result.append(line)
            continue
        
        # Check if this is a list item (unordered)
        is_list_item = bool(re.match(r'^[-*+]\s+', line))
        
        if is_list_item:
            # Check if we need blank line before list start
            if result:
                prev_line = result[-1]
                if prev_line.strip() != "":
                    # Check if previous line is not also a list item or heading
                    prev_is_list = bool(re.match(r'^[-*+]\s+', prev_line))
                    prev_is_heading = prev_line.strip().startswith("#")
                    
                    if not prev_is_list and not prev_is_heading:
                        result.append("")  # Add blank line before list
        
        result.append(line)
        
        # Check if we need blank line after list ends
        if is_list_item and i + 1 < len(lines):
            next_line = lines[i + 1]
            if next_line.strip():  # Next line is not blank
                next_is_list = bool(re.match(r'^[-*+]\s+', next_line))
                next_is_heading = next_line.strip().startswith("#")
                
                if not next_is_list and not next_is_heading:
                    result.append("")  # Add blank line after list
    
    return result


def remove_multiple_blank_lines(lines: List[str]) -> List[str]:
    """Remove multiple consecutive blank lines (MD012)."""
    result = []
    consecutive_blanks = 0
    
    for line in lines:
        if line.strip() == "":
            consecutive_blanks += 1
            if consecutive_blanks <= 1:  # Keep only one blank line
                result.append(line)
        else:
            consecutive_blanks = 0
            result.append(line)
    
    return result


def fix_trailing_spaces(lines: List[str]) -> List[str]:
    """Remove trailing spaces except for intentional line breaks."""
    result = []
    
    for line in lines:
        # Keep intentional two-space line breaks
        if line.endswith("  ") and not line.endswith("   "):
            result.append(line)
        else:
            result.append(line.rstrip())
    
    return result


def fix_markdown_file(content: str) -> str:
    """Apply all markdown fixes to file content."""
    lines = content.splitlines()
    
    # Apply fixes in order
    lines = fix_yaml_front_matter_spacing(lines)
    lines = fix_list_spacing(lines)
    lines = remove_multiple_blank_lines(lines)
    lines = fix_trailing_spaces(lines)
    
    # Ensure file ends with single newline
    result = "\n".join(lines)
    if not result.endswith("\n"):
        result += "\n"
    
    return result


def process_file(path: Path) -> bool:
    """Process a single markdown file and return True if changes were made."""
    try:
        original = path.read_text(encoding="utf-8")
        fixed = fix_markdown_file(original)
        
        if fixed != original:
            path.write_text(fixed, encoding="utf-8")
            print(f"Fixed: {path}")
            return True
        else:
            print(f"No changes needed: {path}")
            return False
    except Exception as e:
        print(f"Error processing {path}: {e}")
        return False


def main(argv: List[str]) -> int:
    """Main function to process command line arguments."""
    if not argv:
        print("Usage: python fix_markdown_lint.py <files...>")
        print("Example: python fix_markdown_lint.py docs/domains/finance/*.md")
        return 1
    
    changed_files = 0
    total_files = 0
    
    for arg in argv:
        path = Path(arg)
        if not path.exists():
            print(f"File not found: {arg}")
            continue
        
        if path.suffix.lower() != ".md":
            print(f"Skipping non-markdown file: {arg}")
            continue
        
        total_files += 1
        if process_file(path):
            changed_files += 1
    
    print(f"\nProcessed {total_files} files, fixed {changed_files} files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
