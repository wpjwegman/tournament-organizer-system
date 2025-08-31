#!/bin/bash
# Tournament Organizer - Professional Podman Development Environment Setup

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Main setup function
main() {
    print_status "🚀 Setting up Tournament Organizer Documentation Environment with Podman"
    
    # Check for Podman
    if ! command -v podman &> /dev/null; then
        print_error "❌ Podman not found. Please install Podman:"
        echo "  https://podman.io/getting-started/installation"
        exit 1
    fi
    
    print_success "✅ Using Podman (enterprise-grade containerization)"
    
    # Set compose command
    COMPOSE_CMD="podman-compose"
    if ! command -v podman-compose &> /dev/null; then
        COMPOSE_CMD="podman compose"
    fi
    
    # Change to documents directory
    cd "$(dirname "$0")"
    
    print_status "🏗️  Building development environment..."
    $COMPOSE_CMD build docs-dev
    
    print_status "🔧 Setting up development tools..."
    
    # Create development aliases
    cat > .env.local << EOF
# Podman development configuration
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
    print_status "🎉 Happy documenting!"
}

# Run main function
main "$@"
