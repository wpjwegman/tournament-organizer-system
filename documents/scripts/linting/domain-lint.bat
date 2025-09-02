@echo off
REM Quick Domain Linting Commands
REM Professional shortcuts for domain-specific markdown linting

cd /d "C:\Projects\Tournament Organizer\documents"

if "%1"=="--help" goto :help
if "%1"=="/?" goto :help
if "%1"=="-h" goto :help
if "%1"=="" goto :help

set DOMAIN=%1
set ACTION=%2

if "%ACTION%"=="" set ACTION=check

echo.
echo ================================================
echo Domain Linting Tool - %DOMAIN% Domain
echo ================================================

if "%ACTION%"=="check" (
    echo 🔍 Checking %DOMAIN% domain...
    python scripts\domain_lint.py %DOMAIN% --check-only --report
) else if "%ACTION%"=="fix" (
    echo 🔧 Fixing %DOMAIN% domain...
    python scripts\domain_lint.py %DOMAIN% --fix --auto-stage --verbose
) else if "%ACTION%"=="report" (
    echo 📊 Generating report for %DOMAIN% domain...
    python scripts\domain_lint.py %DOMAIN% --check-only --save-report --report
) else if "%ACTION%"=="setup" (
    echo 🚀 Setting up Git hooks...
    python scripts\setup_git_hooks.py
) else (
    goto :help
)

goto :end

:help
echo Usage: domain-lint.bat DOMAIN [ACTION]
echo.
echo DOMAIN: finance, tournament, identity, etc.
echo.
echo ACTIONS:
echo   check    Check domain for linting issues (default)
echo   fix      Fix issues and auto-stage changes
echo   report   Generate detailed report
echo   setup    Setup Git pre-commit hooks
echo.
echo Examples:
echo   domain-lint.bat finance
echo   domain-lint.bat finance check
echo   domain-lint.bat finance fix
echo   domain-lint.bat tournament report
echo   domain-lint.bat setup setup
echo.

:end
