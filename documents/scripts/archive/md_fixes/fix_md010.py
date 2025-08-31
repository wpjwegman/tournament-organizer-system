#!/usr/bin/env python3
"""
MD010 Fixer: Hard Tabs to Spaces

Converts hard tabs to spaces in markdown files.
Part of the enterprise automation suite.
"""
import sys


def fix_md010(file_path):
    """Fix MD010: Replace hard tabs with spaces."""
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    # Replace tabs with 4 spaces (standard)
    fixed_content = content.replace("\t", "    ")

    if fixed_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed_content)
        print(f"[MD010] Fixed hard tabs in {file_path}")
        return True
    return False

def main():
    files = sys.argv[1:]
    fixed_count = 0
    for file_path in files:
        if fix_md010(file_path):
            fixed_count += 1

    if fixed_count > 0:
        print(f"[MD010] Fixed {fixed_count} files with hard tabs")
    else:
        print("[MD010] No hard tabs found")

if __name__ == "__main__":
    main()
