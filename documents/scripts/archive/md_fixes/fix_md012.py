import re
import sys

## Removed unused imports


def fix_md012(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    fixed = re.sub(r"\n{3,}", "\n\n", content)
    if fixed != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"[MD012] Fixed multiple blank lines in {file_path}")
        return True
    return False


if __name__ == "__main__":
    files = sys.argv[1:]
    for file_path in files:
        fix_md012(file_path)
