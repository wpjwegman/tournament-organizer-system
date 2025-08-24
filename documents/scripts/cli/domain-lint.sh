#!/bin/bash
# Professional Domain Linting CLI
# Professional shortcuts for domain-specific markdown linting

cd "$(dirname "$0")/../.."

show_help() {
    echo "Professional Domain Linting CLI"
    echo "==============================="
    echo ""
    echo "Usage: ./scripts/cli/domain-lint.sh DOMAIN [ACTION]"
    echo ""
    echo "DOMAIN: finance, tournament, identity, etc."
    echo ""
    echo "ACTIONS:"
    echo "  check    Check domain for linting issues (default)"
    echo "  fix      Fix issues and auto-stage changes"
    echo "  report   Generate detailed report"
    echo "  setup    Setup Git pre-commit hooks"
    echo ""
    echo "Examples:"
    echo "  ./scripts/cli/domain-lint.sh finance"
    echo "  ./scripts/cli/domain-lint.sh finance check"
    echo "  ./scripts/cli/domain-lint.sh finance fix"
    echo "  ./scripts/cli/domain-lint.sh tournament report"
    echo "  ./scripts/cli/domain-lint.sh setup setup"
    echo ""
    echo "Available domains:"
    if [ -d "docs/domains" ]; then
        for domain in docs/domains/*/; do
            if [ -d "$domain" ]; then
                basename "$domain"
            fi
        done | sed 's/^/  /'
    else
        echo "  (no domains found)"
    fi
    echo ""
}

if [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ "$1" = "" ]; then
    show_help
    exit 0
fi

DOMAIN="$1"
ACTION="${2:-check}"

# Validate domain exists
if [ ! -d "docs/domains/$DOMAIN" ]; then
    echo "❌ Domain '$DOMAIN' not found"
    echo ""
    echo "Available domains:"
    if [ -d "docs/domains" ]; then
        for domain in docs/domains/*/; do
            if [ -d "$domain" ]; then
                echo "  $(basename "$domain")"
            fi
        done
    fi
    exit 1
fi

echo ""
echo "================================================"
echo "Professional Domain Linting - $DOMAIN Domain"
echo "================================================"

case "$ACTION" in
    "check")
        echo "🔍 Checking $DOMAIN domain..."
        python scripts/linting/domain_linter.py "$DOMAIN" --check-only --report
        ;;
    "fix")
        echo "🔧 Fixing $DOMAIN domain..."
        python scripts/linting/domain_linter.py "$DOMAIN" --fix --auto-stage --verbose
        ;;
    "report")
        echo "📊 Generating report for $DOMAIN domain..."
        python scripts/linting/domain_linter.py "$DOMAIN" --check-only --save-report --report
        ;;
    "setup")
        echo "🚀 Setting up Git hooks..."
        python scripts/git-hooks/setup_git_hooks.py --install
        ;;
    *)
        echo "❌ Unknown action: $ACTION"
        show_help
        exit 1
        ;;
esac
