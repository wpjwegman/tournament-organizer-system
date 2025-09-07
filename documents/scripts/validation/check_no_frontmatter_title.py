#!/usr/bin/env python3
"""
Fail if any staged Markdown file under documents/docs contains a front-matter 'title:' field.

Usage (pre-commit passes file list):
  python scripts/check_no_frontmatter_title.py [files...]

If no files are passed (e.g., always_run job), the script discovers staged files with git.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "documents" / "docs"

TITLE_RE = re.compile(r"^\s*title:\s*", re.IGNORECASE)


def staged_markdown_files() -> list[Path]:
    try:
        out = subprocess.check_output(["git", "diff", "--cached", "--name-only"], text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    paths = [ROOT / p.strip() for p in out.splitlines() if p.strip().endswith(".md")]
    return [p for p in paths if DOCS_DIR in p.parents or p == DOCS_DIR]


def has_front_matter_title(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except (FileNotFoundError, PermissionError, OSError):
        return False

    # Only scan the YAML front matter block if present at top of file
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        # malformed/incomplete front matter; treat as no title guard here
        return False
    yaml_block = text[3 : end + 1].splitlines()
    return any(TITLE_RE.match(line) for line in yaml_block)


def main(argv: list[str]) -> int:
    files = [Path(p) for p in argv if p.endswith(".md")]
    if not files:
        files = staged_markdown_files()

    offending = [p.relative_to(ROOT) for p in files if p.is_file() and has_front_matter_title(p)]

    if offending:
        print("Found forbidden 'title:' in front matter:", file=sys.stderr)
        for p in offending:
            print(f" - {p}", file=sys.stderr)
        print("Use a visible H1 and remove 'title:' from YAML.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
