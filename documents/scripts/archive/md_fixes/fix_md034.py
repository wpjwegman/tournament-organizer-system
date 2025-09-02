#!/usr/bin/env python3
"""
MD034 Fixer: Bare URL Wrapper

Wraps bare URLs in proper markdown link syntax.
Part of the enterprise automation suite.
"""

import re
import sys


def fix_md034(file_path):
    """Fix MD034: Wrap bare URLs in markdown link syntax."""
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    # Email pattern - wrap in angle brackets
    email_pattern = r"\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b"
    content = re.sub(email_pattern, r"<\1>", content)

    # URL pattern - wrap in angle brackets (for simple URLs)
    # This is conservative - only handles obvious URLs not already in links
    url_pattern = r"(?<![\[\(])(https?://[^\s\)]+|www\.[^\s\)]+\.[a-zA-Z]{2,}[^\s\)]*)(?![\]\)])"
    content = re.sub(url_pattern, r"<\1>", content)

    with open(file_path, encoding="utf-8") as f:
        original_content = f.read()

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[MD034] Fixed bare URLs in {file_path}")
        return True
    return False


def main():
    files = sys.argv[1:]
    fixed_count = 0
    for file_path in files:
        if fix_md034(file_path):
            fixed_count += 1

    if fixed_count > 0:
        print(f"[MD034] Fixed {fixed_count} files with bare URLs")
    else:
        print("[MD034] No bare URLs found")


if __name__ == "__main__":
    main()
