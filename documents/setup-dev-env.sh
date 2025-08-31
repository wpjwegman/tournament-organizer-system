#!/bin/bash
# Professional development environment setup script
# Supports both Docker and Podman

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Detect container runtime
detect_container_runtime() {
    if command -v podman &> /dev/null; then
        echo "podman"
    elif command -v docker &> /dev/null; then
        echo "docker"
    else
        echo "none"
    fi
}

# Print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Main setup function
main() {
    print_status "🚀 Setting up Tournament Organizer Documentation Environment"
    
    # Detect container runtime
    CONTAINER_RUNTIME=$(detect_container_runtime)
    
    case $CONTAINER_RUNTIME in
        "podman")
            print_success "✅ Using Podman (recommended for enterprise environments)"
            COMPOSE_CMD="podman-compose"
            if ! command -v podman-compose &> /dev/null; then
                print_warning "⚠️  podman-compose not found, using podman compose"
                COMPOSE_CMD="podman compose"
            fi
            ;;
        "docker")
            print_success "✅ Using Docker"
            COMPOSE_CMD="docker compose"
            if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
                print_error "❌ Docker Compose not available"
                exit 1
            fi
            ;;
        "none")
            print_error "❌ Neither Podman nor Docker found. Please install one of them:"
            echo "  - Podman (recommended): https://podman.io/getting-started/installation"
            echo "  - Docker: https://docs.docker.com/get-docker/"
            exit 1
            ;;
    esac
    
    # Change to documents directory
    cd "$(dirname "$0")"
    
    print_status "🏗️  Building development environment..."
    $COMPOSE_CMD build docs-dev
    
    print_status "🔧 Setting up development tools..."
    
    # Create development aliases
    cat > .env.local << EOF
# Container runtime configuration
CONTAINER_RUNTIME=$CONTAINER_RUNTIME
COMPOSE_CMD=$COMPOSE_CMD

# Development aliases (source this file or add to your shell rc)
alias docs-dev='$COMPOSE_CMD run --rm docs-dev'
alias docs-serve='$COMPOSE_CMD up docs-serve'
alias docs-qa='$COMPOSE_CMD run --rm docs-qa'
alias docs-lint='$COMPOSE_CMD run --rm docs-dev uv run pre-commit run --all-files'
alias docs-build='$COMPOSE_CMD run --rm docs-dev uv run mkdocs build --strict'
alias docs-domain-lint='$COMPOSE_CMD run --rm docs-dev uv run python scripts/linting/domain_linter.py'
EOF
    
    print_success "✅ Environment setup complete!"
    print_status "📖 Available commands:"
    echo ""
    echo "  🖥️  Development shell:     $COMPOSE_CMD run --rm docs-dev"
    echo "  🌐 Serve documentation:   $COMPOSE_CMD up docs-serve"
    echo "  🔍 Run quality checks:    $COMPOSE_CMD run --rm docs-qa"
    echo "  📋 Run linting:           $COMPOSE_CMD run --rm docs-dev uv run pre-commit run --all-files"
    echo "  🏗️  Build documentation:   $COMPOSE_CMD run --rm docs-dev uv run mkdocs build --strict"
    echo "  🎯 Domain-specific lint:  $COMPOSE_CMD run --rm docs-dev uv run python scripts/linting/domain_linter.py [domain]"
    echo ""
    echo "  💡 Source environment:     source .env.local"
    echo ""
    print_status "🎉 Happy documenting!"
}

# Run main function
main "$@"
