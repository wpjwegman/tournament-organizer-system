import os
import subprocess
import sys

## Removed unused import

FIXERS = [
    "fix_md005.py",  # Inconsistent list indentation
    "fix_md007.py",  # Unordered list indentation
    "fix_md010.py",  # Hard tabs
    "fix_md012.py",  # Multiple consecutive blank lines
    "fix_md022.py",  # Headings surrounded by blank lines
    "fix_md025.py",  # Multiple top-level headings
    "fix_md031.py",  # Fenced code blocks surrounded by blank lines
    "fix_md032.py",  # Lists surrounded by blank lines
    "fix_md034.py",  # Bare URLs
    "fix_md041.py",  # First line heading requirement
    "fix_md047.py",  # Files should end with single newline
    "fix_md049.py",  # Emphasis style standardization
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def find_markdown_files(root_dir, domain=None):
    # If domain is a path, use as is; if just a name, join with docs/domains
    if domain:
        if os.path.sep in domain or "/" in domain:
            search_dir = os.path.join(root_dir, domain)
        else:
            search_dir = os.path.join(root_dir, "documents", "docs", "domains", domain)
    else:
        search_dir = root_dir
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.endswith(".md"):
                yield os.path.join(root, file)


def run_fixer(fixer, files):
    fixer_path = os.path.join(SCRIPT_DIR, fixer)
    print(f"\nRunning {fixer}...")
    for file in files:
        subprocess.run([sys.executable, fixer_path, file], check=False)


def run_linter(domain=None, stage="before"):
    print(f"\n--- Linting Report ({stage}) ---")
    # Use the updated domain_linter.py which now uses markdownlint-cli2
    linter_path = os.path.join("documents", "scripts", "linting", "domain_linter.py")
    cmd = [sys.executable, linter_path]
    # Only pass domain name, not path
    if domain:
        domain_arg = os.path.basename(domain) if os.path.sep in domain or "/" in domain else domain
        cmd.append(domain_arg)
    cmd += ["--check-only", "--threshold", "0", "--verbose", "--report"]
    subprocess.run(cmd, check=False)

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_all_md_fixes.py <root_dir> [domain]")
        sys.exit(1)
    root_dir = sys.argv[1]
    domain = sys.argv[2] if len(sys.argv) > 2 else None
    files = list(find_markdown_files(root_dir, domain))
    print(f"Found {len(files)} markdown files.")
    # Run linter before fixes
    run_linter(domain, "before")
    before = {f: open(f, encoding="utf-8").read() for f in files}
    for fixer in FIXERS:
        run_fixer(fixer, files)
    # Run linter after fixes
    run_linter(domain, "after")
    after = {f: open(f, encoding="utf-8").read() for f in files}
    print("\n--- Before/After Evaluation ---")
    for f in files:
        if before[f] != after[f]:
            print(f"[CHANGED] {f}")
        else:
            print(f"[UNCHANGED] {f}")
    print("\nAll fixers executed. Ready for pre-commit integration.")

if __name__ == "__main__":
    main()
