import re
import sys


def fix_md025(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    h1_count = 0
    fixed_lines = []
    for line in lines:
        if re.match(r"^# ", line):
            h1_count += 1
            if h1_count == 1:
                fixed_lines.append(line)
            else:
                # Demote additional H1s to H2
                fixed_lines.append("##" + line[1:])
        else:
            fixed_lines.append(line)
    fixed = "".join(fixed_lines)
    with open(file_path, encoding="utf-8") as f:
        orig = f.read()
    if fixed != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"[MD025] Fixed multiple top-level headings in {file_path}")
        return True
    return False


if __name__ == "__main__":
    files = sys.argv[1:]
    for file_path in files:
        fix_md025(file_path)
