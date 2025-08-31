@echo off
REM Professional development environment setup script for Windows
REM Supports both Docker and Podman

setlocal enabledelayedexpansion

echo [INFO] 🚀 Setting up Tournament Organizer Documentation Environment

REM Detect container runtime
where podman >nul 2>&1
if %ERRORLEVEL% == 0 (
    set CONTAINER_RUNTIME=podman
    set COMPOSE_CMD=podman-compose
    where podman-compose >nul 2>&1
    if !ERRORLEVEL! NEQ 0 (
        set COMPOSE_CMD=podman compose
    )
    echo [SUCCESS] ✅ Using Podman (recommended for enterprise environments)
) else (
    where docker >nul 2>&1
    if !ERRORLEVEL! == 0 (
        set CONTAINER_RUNTIME=docker
        set COMPOSE_CMD=docker compose
        docker compose version >nul 2>&1
        if !ERRORLEVEL! NEQ 0 (
            echo [ERROR] ❌ Docker Compose not available
            exit /b 1
        )
        echo [SUCCESS] ✅ Using Docker
    ) else (
        echo [ERROR] ❌ Neither Podman nor Docker found. Please install one of them:
        echo   - Podman (recommended): https://podman.io/getting-started/installation
        echo   - Docker: https://docs.docker.com/get-docker/
        exit /b 1
    )
)

REM Change to documents directory
cd /d "%~dp0"

echo [INFO] 🏗️  Building development environment...
%COMPOSE_CMD% build docs-dev

echo [INFO] 🔧 Setting up development tools...

REM Create development aliases
(
echo # Container runtime configuration
echo CONTAINER_RUNTIME=%CONTAINER_RUNTIME%
echo COMPOSE_CMD=%COMPOSE_CMD%
echo.
echo # Development aliases for PowerShell (add to your profile)
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
echo   💡 Source environment:     . .\.env.local
echo.
echo [INFO] 🎉 Happy documenting!
