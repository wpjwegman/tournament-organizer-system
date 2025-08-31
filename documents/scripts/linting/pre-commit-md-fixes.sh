#!/usr/bin/env bash
# Enterprise-grade pre-commit hook for markdown linting
# Uses markdownlint-cli2 and custom domain-specific fixers
set -e

# Configuration
DOMAIN="${2:-identity}"  # Default to identity domain
ROOT_DIR="${1:-.}"
SCRIPT_DIR="$(dirname "$0")/md_fixes"

echo "🔧 Running enterprise markdown linting for domain: $DOMAIN"

# Check if markdownlint-cli2 is available
if ! command -v markdownlint-cli2 &> /dev/null; then
    echo "❌ markdownlint-cli2 not found. Install with: npm install -g markdownlint-cli2"
    exit 1
fi

# Run the orchestrator with domain-specific linting
if [ -f "$SCRIPT_DIR/run_all_md_fixes.py" ]; then
    python "$SCRIPT_DIR/run_all_md_fixes.py" "$ROOT_DIR" "$DOMAIN"
    
    # Check if there are any changes to stage
    if git diff --quiet documents/docs/domains/"$DOMAIN"/ 2>/dev/null; then
        echo "✅ No markdown fixes needed"
    else
        echo "📝 Markdown fixes applied - staging changes"
        git add documents/docs/domains/"$DOMAIN"/**/*.md 2>/dev/null || true
    fi
else
    echo "❌ Orchestrator script not found: $SCRIPT_DIR/run_all_md_fixes.py"
    exit 1
fi

echo "🎉 Enterprise markdown linting completed successfully"
