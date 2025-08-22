#!/usr/bin/env python3
"""
Lightweight Markdown auto-fix for low-risk issues:
- Trim trailing spaces (except for two-space line breaks)
- Ensure a single final newline
- Add language to fenced code blocks when obviously detectable (``` -> ```text)
- Ensure exactly one blank line around fenced code blocks (before and after)
- Ensure exactly one blank line above and below ATX headings (#, ##, ...); first content line after front matter may be a heading without a blank above
- Avoid modifying content inside fenced code blocks except for fence lines themselves

Usage: pre-commit passes filenames; you can also run manually:
    python documents/scripts/markdown_autofix.py <files...>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Fenced code blocks: support language after opening fence
FENCE_ANY_RE = re.compile(r"^```(\S*)\s*$")  # captures language or empty
ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+).+")


def fix_markdown(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False
    i = 0

    # detect front matter block at top by indexes in original lines
    fm_end_index = -1
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                fm_end_index = j
                break

    was_list_line = False

    def append_blank_once():
        if not out or out[-1].strip() != "":
            out.append("")

    # Skip any leading blank lines entirely (no initial blank at top)
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    while i < len(lines):
        line = lines[i]

        # Detect any fence line (opening or closing)
        m = FENCE_ANY_RE.match(line)
        if m:
            lang = m.group(1)
            if not in_fence:
                # Opening fence
                if out and out[-1].strip() != "":
                    out.append("")
                if lang == "":
                    out.append("```text")
                else:
                    out.append(f"```{lang}")
                in_fence = True
            else:
                # Closing fence
                in_fence = False
                out.append("```")
                # ensure one blank after, unless EOF or next is already blank
                next_line = lines[i + 1] if i + 1 < len(lines) else None
                if next_line is not None and next_line.strip() != "":
                    out.append("")
            i += 1
            continue

        # Ensure exactly one blank line around ATX headings, except directly after front matter
        if ATX_HEADING_RE.match(line) and not in_fence:
            # remove extra blanks before
            while out and out[-1].strip() == "":
                out.pop()
            # add a single blank before unless this is first content line or directly after front matter
            if i != 0 and i != fm_end_index + 1:
                append_blank_once()
            out.append(line.rstrip(" "))
            # ensure a single blank after if next line isn't blank or a fence
            next_line = lines[i + 1] if i + 1 < len(lines) else None
            if next_line is not None and next_line.strip() != "" and not FENCE_ANY_RE.match(next_line):
                out.append("")
            i += 1
            was_list_line = False
            continue

        # Ensure blank line before list start when previous non-blank isn't a list/heading/fence
        if LIST_ITEM_RE.match(line) and not in_fence:
            prev = out[-1] if out else ""
            if prev.strip() != "" and not LIST_ITEM_RE.match(prev) and not ATX_HEADING_RE.match(prev) and not FENCE_ANY_RE.match(prev):
                out.append("")
            was_list_line = True

        # Trim trailing spaces but keep two-space line breaks
        if line.rstrip(" ") != line:
            if line.endswith("  ") and not line.endswith("   "):
                line = line.rstrip(" ") + "  "
            else:
                line = line.rstrip(" ")

        # Collapse multiple blank lines outside fences
        if not in_fence and line.strip() == "":
            append_blank_once()
            i += 1
            continue

        # Ensure a blank after a list block when the current line is not a list item
        if not LIST_ITEM_RE.match(line) and was_list_line and not in_fence:
            if out and out[-1].strip() != "":
                out.append("")
            was_list_line = False

        out.append(line)
        i += 1

    fixed = "\n".join(out)
    if not fixed.endswith("\n"):
        fixed += "\n"
    return fixed


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8", errors="ignore")
    fixed = fix_markdown(original)
    if fixed != original:
        path.write_text(fixed, encoding="utf-8")
        return True
    return False


def main(argv: list[str]) -> int:
    changed = False
    for arg in argv:
        p = Path(arg)
        if p.suffix.lower() != ".md" or not p.exists():
            continue
        if process_file(p):
            changed = True
    return 0 if not changed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
