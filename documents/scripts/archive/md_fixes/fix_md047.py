import sys

## Removed unused import

def fix_md047(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    # Remove trailing blank lines, ensure single newline
    fixed = content.rstrip(b"\r\n") + b"\n"
    if fixed != content:
        with open(file_path, "wb") as f:
            f.write(fixed)
        print(f"[MD047] Fixed trailing newline in {file_path}")
        return True
    return False

if __name__ == "__main__":
    files = sys.argv[1:]
    for file_path in files:
        fix_md047(file_path)
