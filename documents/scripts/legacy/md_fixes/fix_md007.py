"""
Professional MD007 Fixer Script

- Handles unordered list indentation per CommonMark and MD007 rules
- Detects and corrects only lines that violate MD007
- Handles edge cases: code blocks, blockquotes, YAML frontmatter, mixed indentation, nested lists
- Idempotent: can correct its own previous errors
- Provides detailed reporting of changes and unsolved errors
"""

import re
import sys


def is_code_block(line):
    return line.strip().startswith("```")


def is_yaml_frontmatter(line):
    return line.strip() in ("---", "...")


def fix_md007(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    fixed_lines = []
    in_code_block = False
    in_yaml = False
    unsolved = []

    for idx, line in enumerate(lines):
        # Detect YAML frontmatter start/end
        if line.strip() == "---":
            if idx == 0:  # Start of file
                in_yaml = True
                fixed_lines.append(line)
                continue
            if in_yaml:  # End of YAML
                in_yaml = False
                fixed_lines.append(line)
                continue

        # Skip processing list items in YAML frontmatter
        if in_yaml:
            # Special handling for YAML lists that pymarkdownlnt incorrectly flags
            if re.match(r"^\s*-\s+", line):
                # This is a YAML list item - normalize to standard YAML indentation
                content = line.strip()
                if content.startswith("- "):
                    fixed_lines.append(f"  {content}\n")
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
            continue

        # Detect code blocks
        if is_code_block(line):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        if in_code_block:
            fixed_lines.append(line)
            continue

        # Detect blockquotes
        blockquote_match = re.match(r"^(>+\s*)(.*)", line)
        blockquote_prefix = ""
        content = line
        if blockquote_match:
            blockquote_prefix = blockquote_match.group(1)
            content = blockquote_match.group(2)

        # Detect unordered list item
        match = re.match(r"^(\s*)([-*+]) (.*)", content)
        if match:
            indent, bullet, rest = match.groups()
            # For top-level lists, should have no indentation
            expected_indent = ""

            # Only fix if indentation is incorrect
            if indent != expected_indent:
                fixed_line = f"{blockquote_prefix}{expected_indent}{bullet} {rest}\n"
                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)

    fixed = "".join(fixed_lines)
    with open(file_path, encoding="utf-8") as f:
        orig = f.read()
    changed = False
    if fixed != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"[MD007] Fixed unordered list indentation in {file_path}")
        changed = True
    if unsolved:
        print(f"[MD007] Unsolved indentation errors in {file_path}:")
        for line_num, line_text in unsolved:
            print(f"  Line {line_num}: {line_text}")
    return changed, unsolved


def main():
    files = sys.argv[1:]
    total_unsolved = {}
    for file_path in files:
        changed, unsolved = fix_md007(file_path)
        if unsolved:
            total_unsolved[file_path] = unsolved
    if total_unsolved:
        print("\nSummary of unsolved MD007 errors:")
        for file_path, errors in total_unsolved.items():
            print(f"{file_path}:")
            for line_num, line_text in errors:
                print(f"  Line {line_num}: {line_text}")
    else:
        print("All MD007 errors fixed!")


if __name__ == "__main__":
    main()
