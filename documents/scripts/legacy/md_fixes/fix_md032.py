import re
import sys

## Removed unused import


def fix_md032(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*[-*+] ", line):
            # Ensure blank line before
            if fixed_lines and fixed_lines[-1].strip() != "":
                fixed_lines.append("\n")
            # Add list lines
            while i < len(lines) and re.match(r"^\s*[-*+] ", lines[i]):
                fixed_lines.append(lines[i])
                i += 1
            # Ensure blank line after
            if i < len(lines) and lines[i].strip() != "":
                fixed_lines.append("\n")
            continue
        fixed_lines.append(line)
        i += 1
    fixed = "".join(fixed_lines)
    with open(file_path, encoding="utf-8") as f:
        orig = f.read()
    if fixed != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"[MD032] Fixed list blank lines in {file_path}")
        return True
    return False


if __name__ == "__main__":
    files = sys.argv[1:]
    for file_path in files:
        fix_md032(file_path)
