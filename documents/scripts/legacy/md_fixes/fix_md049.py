#!/usr/bin/env python3
"""
MD049 Fixer: Emphasis Style Standardization

Converts underscore emphasis to asterisk emphasis for consistency.
Part of the enterprise automation suite.
"""

import re
import sys


def fix_md049(file_path) -> bool:
    """Fix MD049: Convert underscore emphasis to asterisk."""
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    # Convert _text_ to *text* (single emphasis)
    content = re.sub(r"(?<!\w)_([^_\n]+?)_(?!\w)", r"*\1*", content)

    # Convert __text__ to **text** (strong emphasis)
    content = re.sub(r"(?<!\w)__([^_\n]+?)__(?!\w)", r"**\1**", content)

    with open(file_path, encoding="utf-8") as f:
        original_content = f.read()

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[MD049] Fixed emphasis style in {file_path}")
        return True
    return False


def main() -> None:
    files = sys.argv[1:]
    fixed_count = 0
    for file_path in files:
        if fix_md049(file_path):
            fixed_count += 1

    if fixed_count > 0:
        print(f"[MD049] Fixed {fixed_count} files with underscore emphasis")
    else:
        print("[MD049] No underscore emphasis found")


if __name__ == "__main__":
    main()
