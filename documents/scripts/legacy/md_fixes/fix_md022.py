import re
import sys

## Removed unused import


def fix_md022(file_path) -> bool:
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^#{1,6} ", line):
            # Ensure one blank line before
            if fixed_lines and fixed_lines[-1].strip() != "":
                fixed_lines.append("\n")
            fixed_lines.append(line)
            # Ensure one blank line after
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                fixed_lines.append("\n")
        else:
            fixed_lines.append(line)
        i += 1
    fixed = "".join(fixed_lines)
    with open(file_path, encoding="utf-8") as f:
        orig = f.read()
    if fixed != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"[MD022] Fixed heading blank lines in {file_path}")
        return True
    return False


if __name__ == "__main__":
    files = sys.argv[1:]
    for file_path in files:
        fix_md022(file_path)
