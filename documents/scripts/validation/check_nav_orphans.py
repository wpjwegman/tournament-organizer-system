#!/usr/bin/env python3
"""
Fail if MkDocs reports pages under docs/ that are not listed in mkdocs.yml nav.
Runs a mkdocs build (non-strict), captures stdout, and searches for the known
marker line emitted by MkDocs:

  "The following pages exist in the docs directory, but are not included in the \"nav\" configuration:"

If found, prints the list and exits with non-zero.
"""
from __future__ import annotations
import subprocess
import sys
import re

MARKER = 'The following pages exist in the docs directory, but are not included in the "nav" configuration:'

def main() -> int:
    try:
        # Build once; rely on project mkdocs.yml in current working directory
        proc = subprocess.run(
            [sys.executable, '-m', 'mkdocs', 'build', '--no-directory-urls'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
    except Exception as e:
        print(f"mkdocs build failed to run: {e}", file=sys.stderr)
        return 2

    out = proc.stdout or ''
    print(out)

    if MARKER in out:
        print("\nERROR: Pages found outside nav. Add them to mkdocs.yml nav or move/remove from docs/.", file=sys.stderr)
        # Extract indented list items immediately following the marker
        lines = out.splitlines()
        try:
            idx = next(i for i, line in enumerate(lines) if MARKER in line)
        except StopIteration:
            idx = -1
        if idx >= 0:
            for line in lines[idx+1:]:
                if re.match(r"^\s+- ", line):
                    print(line, file=sys.stderr)
                else:
                    break
        return 1

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
