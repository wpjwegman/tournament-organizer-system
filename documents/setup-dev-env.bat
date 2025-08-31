@echo off
REM Tournament Organizer - Professional Podman Development Environment Setup

setlocal enabledelayedexpansion

echo [INFO] Setting up Tournament Organizer Documentation Environment with Podman

REM Check for Podman
where podman >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Podman not found. Please install Podman Desktop:
    echo   https://podman.io/getting-started/installation
    exit /b 1
)

echo [SUCCESS] Using Podman (enterprise-grade containerization)

REM Set compose command
set COMPOSE_CMD=podman-compose
where podman-compose >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    set COMPOSE_CMD=podman compose
)

REM Change to documents directory
cd /d "%~dp0"

echo [INFO] 🏗️  Building development environment...
%COMPOSE_CMD% build docs-dev

echo [INFO] 🔧 Setting up development tools...

REM Create development aliases
(
echo # Podman development configuration
echo COMPOSE_CMD=%COMPOSE_CMD%
echo.
echo # Development aliases for PowerShell
echo function docs-dev { %COMPOSE_CMD% run --rm docs-dev $args }
echo function docs-serve { %COMPOSE_CMD% up docs-serve }
echo function docs-qa { %COMPOSE_CMD% run --rm docs-qa }
echo function docs-lint { %COMPOSE_CMD% run --rm docs-dev uv run pre-commit run --all-files }
echo function docs-build { %COMPOSE_CMD% run --rm docs-dev uv run mkdocs build --strict }
echo function docs-domain-lint { %COMPOSE_CMD% run --rm docs-dev uv run python scripts/linting/domain_linter.py $args }
) > .env.local

echo [SUCCESS] ✅ Environment setup complete!
echo [INFO] 📖 Available commands:
echo.
echo   🖥️  Development shell:     %COMPOSE_CMD% run --rm docs-dev
echo   🌐 Serve documentation:   %COMPOSE_CMD% up docs-serve
echo   🔍 Run quality checks:    %COMPOSE_CMD% run --rm docs-qa
echo   📋 Run linting:           %COMPOSE_CMD% run --rm docs-dev uv run pre-commit run --all-files
echo   🏗️  Build documentation:   %COMPOSE_CMD% run --rm docs-dev uv run mkdocs build --strict
echo   🎯 Domain-specific lint:  %COMPOSE_CMD% run --rm docs-dev uv run python scripts/linting/domain_linter.py [domain]
echo.
echo [INFO] 🎉 Happy documenting!
