#!/usr/bin/env python3
"""
Fix Markdownlint Errors Script
=============================

This script fixes all the specific markdownlint-cli2 errors found in CI/CD.
"""

import os
import re
import glob


def fix_code_blocks():
    """Fix fenced code blocks without language specification."""
    print("🔧 Fixing code blocks without language...")
    
    files_to_fix = [
        "architecture/backend/README.md",
        "architecture/frontend/README.md", 
        "architecture/overview.md"
    ]
    
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace ``` with ```text for generic content
            # This is a simple approach - more sophisticated logic could be added
            content = re.sub(r'\n```\n', '\n```text\n', content)
            content = re.sub(r'^```\n', '```text\n', content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✅ Fixed: {file_path}")


def fix_table_column_count():
    """Fix table column count issues."""
    print("🔧 Fixing table column count...")
    
    files_with_tables = [
        "docs/domains/safety/incident.md",
        "docs/domains/safety/safety.md",
        "docs/domains/schedule/match.md"
    ]
    
    for file_path in files_with_tables:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            fixed_lines = []
            in_table = False
            
            for line in lines:
                # Simple table detection and fixing
                if '|' in line and line.strip().startswith('|'):
                    # Count pipes to determine columns
                    pipe_count = line.count('|')
                    if pipe_count < 6:  # Less than expected 5 columns + border pipes
                        # Add missing columns with empty data
                        missing_cols = 6 - pipe_count
                        if line.strip().endswith('|'):
                            line = line.rstrip() + ' |' * missing_cols + '\n'
                        else:
                            line = line.rstrip() + ' |' * (missing_cols + 1) + '\n'
                    
                fixed_lines.append(line)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(fixed_lines)
            
            print(f"  ✅ Fixed: {file_path}")


def fix_emphasis_style():
    """Fix emphasis style (underscore to asterisk)."""
    print("🔧 Fixing emphasis style...")
    
    file_path = "docs/domains/venue/area.md"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace _text_ with *text*
        content = re.sub(r'_([^_\s]+)_', r'*\1*', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Fixed: {file_path}")


def fix_heading_spacing():
    """Fix heading spacing issues."""
    print("🔧 Fixing heading spacing...")
    
    file_path = "scripts/linting/ENTERPRISE_SETUP.md"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        fixed_lines = []
        prev_line = ""
        
        for i, line in enumerate(lines):
            # Add blank line before heading if missing
            if line.startswith('###') and prev_line.strip() and not prev_line.strip() == "":
                if prev_line.strip() and not prev_line.isspace():
                    fixed_lines.append('\n')
            
            # Add blank lines around fenced code blocks
            if line.strip() == '```bash' or line.strip() == '```':
                if prev_line.strip() and not prev_line.isspace():
                    fixed_lines.append('\n')
                fixed_lines.append(line)
                # Look ahead for next line
                if i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].isspace():
                    if not lines[i + 1].startswith('```'):
                        fixed_lines.append('\n')
                continue
            
            # Add blank lines around lists
            if (line.startswith('- ') and prev_line.strip() and 
                not prev_line.startswith('- ') and not prev_line.isspace()):
                fixed_lines.append('\n')
            
            fixed_lines.append(line)
            prev_line = line
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(fixed_lines)
        
        print(f"  ✅ Fixed: {file_path}")


def main():
    """Main execution function."""
    print("🚀 Starting Markdownlint Error Fixes")
    print("=" * 40)
    
    fix_code_blocks()
    print()
    
    fix_table_column_count()
    print()
    
    fix_emphasis_style()
    print()
    
    fix_heading_spacing()
    print()
    
    print("🎉 Markdownlint Error Fixes Completed!")


if __name__ == "__main__":
    main()
