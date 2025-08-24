@echo off
REM Comprehensive Markdown Linting Tool
REM Professional solution for documentation linting with proper configuration

cd /d "C:\Projects\Tournament Organizer\documents"

echo.
echo ================================================
echo Comprehensive Markdown Documentation Linter
echo ================================================
echo.

if "%1"=="--help" goto :help
if "%1"=="/?" goto :help
if "%1"=="-h" goto :help

REM Default: Check finance domain
if "%1"=="" (
    echo Running default check on finance domain...
    python scripts\comprehensive_markdown_lint.py --domain finance --verbose
    goto :end
)

REM Parse arguments and run
python scripts\comprehensive_markdown_lint.py %*
goto :end

:help
echo Usage: lint-docs.bat [options]
echo.
echo Options:
echo   --check-only        Run lint check without fixing
echo   --domain DOMAIN     Process specific domain (e.g., finance)
echo   --all-domains      Process all domain files
echo   --all-files        Process ALL markdown files in repository
echo   --fix              Apply automatic fixes
echo   --verbose          Detailed output
echo.
echo Examples:
echo   lint-docs.bat                           Check finance domain
echo   lint-docs.bat --all-domains --fix      Fix all domain files
echo   lint-docs.bat --all-files --check-only Check entire repository
echo   lint-docs.bat --domain tournament --fix Fix tournament domain
echo.

:end
pause
