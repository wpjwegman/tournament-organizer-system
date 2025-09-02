#!/bin/bash
# Quick Domain Linting Commands
# Professional shortcuts for domain-specific markdown linting

cd "$(dirname "$0")/.."

show_help() {
    echo "Usage: ./scripts/domain-lint.sh DOMAIN [ACTION]"
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
    echo "  ./scripts/domain-lint.sh finance"
    echo "  ./scripts/domain-lint.sh finance check"
    echo "  ./scripts/domain-lint.sh finance fix"
    echo "  ./scripts/domain-lint.sh tournament report"
    echo "  ./scripts/domain-lint.sh setup setup"
    echo ""
}

if [ "$1" = "--help" ] || [ "$1" = "-h" ] || [ "$1" = "" ]; then
    show_help
    exit 0
fi

DOMAIN="$1"
ACTION="${2:-check}"

echo ""
echo "================================================"
echo "Domain Linting Tool - $DOMAIN Domain"
echo "================================================"

case "$ACTION" in
    "check")
        echo "🔍 Checking $DOMAIN domain..."
        python scripts/domain_lint.py "$DOMAIN" --check-only --report
        ;;
    "fix")
        echo "🔧 Fixing $DOMAIN domain..."
        python scripts/domain_lint.py "$DOMAIN" --fix --auto-stage --verbose
        ;;
    "report")
        echo "📊 Generating report for $DOMAIN domain..."
        python scripts/domain_lint.py "$DOMAIN" --check-only --save-report --report
        ;;
    "setup")
        echo "🚀 Setting up Git hooks..."
        python scripts/setup_git_hooks.py
        ;;
    *)
        echo "❌ Unknown action: $ACTION"
        show_help
        exit 1
        ;;
esac
