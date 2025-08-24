#!/bin/bash
# Git pre-commit hook for domain-specific markdown linting
# Place this file in .git/hooks/pre-commit and make it executable

# Configuration
DOCUMENTS_DIR="documents"
DOMAIN_LINT_SCRIPT="scripts/linting/domain_linter.py"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔍 Running domain-specific markdown linting...${NC}"

# Get list of modified .md files in docs/domains/
modified_files=$(git diff --cached --name-only --diff-filter=ACM | grep '^documents/docs/domains/.*\.md$')

if [ -z "$modified_files" ]; then
    echo -e "${GREEN}✅ No domain markdown files modified${NC}"
    exit 0
fi

# Extract unique domains from modified files
domains=$(echo "$modified_files" | sed 's|documents/docs/domains/\([^/]*\)/.*|\1|' | sort -u)

echo -e "${YELLOW}📁 Modified domains: $(echo $domains | tr '\n' ' ')${NC}"

# Check each domain
failed_domains=""
cd "$DOCUMENTS_DIR" || exit 1

for domain in $domains; do
    echo -e "\n${YELLOW}🎯 Checking $domain domain...${NC}"
    
    # Run domain linting with threshold (allow some errors for domains under development)
    if python "$DOMAIN_LINT_SCRIPT" "$domain" --check-only --threshold 10; then
        echo -e "${GREEN}✅ $domain domain passed${NC}"
    else
        echo -e "${RED}❌ $domain domain failed linting${NC}"
        echo -e "${YELLOW}💡 Run: python $DOMAIN_LINT_SCRIPT $domain --fix --auto-stage${NC}"
        failed_domains="$failed_domains $domain"
    fi
done

# Check if any domains failed
if [ -n "$failed_domains" ]; then
    echo -e "\n${RED}❌ Commit blocked due to linting failures in:$failed_domains${NC}"
    echo -e "${YELLOW}Fix the issues and try again.${NC}"
    exit 1
fi

echo -e "\n${GREEN}🎉 All domain markdown files pass linting!${NC}"
exit 0
