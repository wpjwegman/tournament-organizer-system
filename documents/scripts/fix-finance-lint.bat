@echo off
REM Batch script to fix markdown linting issues in finance domain
REM Usage: fix-finance-lint.bat

cd /d "C:\Projects\Tournament Organizer\documents"

echo Fixing markdown linting issues in Finance domain...
echo.

for %%f in (docs\domains\finance\*.md) do (
    echo Processing %%f...
    python scripts\fix_markdown_lint.py "%%f"
)

echo.
echo Running lint check to verify fixes...
uv run pymarkdownlnt scan docs\domains\finance\ --config .pymarkdown.json

echo.
echo Done! Check the results above.
pause
