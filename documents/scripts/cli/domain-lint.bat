@echo off
REM Professional Domain Linting CLI
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
echo Professional Domain Linting - %DOMAIN% Domain
echo ================================================

REM Validate domain exists
if not exist "docs\domains\%DOMAIN%" (
    echo ❌ Domain '%DOMAIN%' not found
    echo Available domains:
    for /d %%i in (docs\domains\*) do echo    %%~ni
    goto :end
)

if "%ACTION%"=="check" (
    echo 🔍 Checking %DOMAIN% domain...
    python scripts\linting\domain_linter.py %DOMAIN% --check-only --report
) else if "%ACTION%"=="fix" (
    echo 🔧 Fixing %DOMAIN% domain...
    python scripts\linting\domain_linter.py %DOMAIN% --fix --auto-stage --verbose
) else if "%ACTION%"=="report" (
    echo 📊 Generating report for %DOMAIN% domain...
    python scripts\linting\domain_linter.py %DOMAIN% --check-only --save-report --report
) else if "%ACTION%"=="setup" (
    echo 🚀 Setting up Git hooks...
    python scripts\git-hooks\setup_git_hooks.py --install
) else (
    goto :help
)

goto :end

:help
echo Professional Domain Linting CLI
echo ================================
echo.
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
echo Available domains:
for /d %%i in (docs\domains\*) do echo   %%~ni
echo.

:end
