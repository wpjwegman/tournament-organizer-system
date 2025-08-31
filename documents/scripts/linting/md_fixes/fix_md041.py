import sys
import re
## Removed unused import

def fix_md041(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Find YAML frontmatter end
    i = 0
    if lines and lines[0].strip() == '---':
        i += 1
        while i < len(lines) and lines[i].strip() != '---':
            i += 1
        i += 1
    # Find first non-blank line
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    # Check if it's a top-level heading
    if i < len(lines) and not re.match(r'^# ', lines[i]):
        lines.insert(i, '# Title\n')
        print(f"[MD041] Inserted top-level heading in {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True
    return False

if __name__ == "__main__":
    files = sys.argv[1:]
    for file_path in files:
        fix_md041(file_path)
