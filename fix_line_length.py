#!/usr/bin/env python3
"""
Targeted fix for remaining line length issues in documentation-style-link.instructions.md
"""

import re
from pathlib import Path

def fix_github_instructions_line_length():
    """Fix line length issues in GitHub instructions"""
    file_path = Path('.github/instructions/documentation-style-link.instructions.md')
    
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply specific line fixes
    fixes = [
        # Line 29 - Scope section
        {
            'find': 'Comprehensive guidelines for writing clear, professional, consistently formatted,\nand well-linked documentation for the project.',
            'replace': 'Comprehensive guidelines for writing clear, professional, consistently\nformatted, and well-linked documentation for the project.'
        },
        # Line 32 - MANDATORY section
        {
            'find': '- Visible H1 titles: Every Markdown page MUST begin its content with a visible H1 heading (first body line after front matter): `# Page Title`.',
            'replace': '- Visible H1 titles: Every Markdown page MUST begin its content with a\n  visible H1 heading (first body line after front matter): `# Page Title`.'
        },
        # Line 41 - Frontmatter tags
        {
            'find': '- Frontmatter tags MUST be provided for all pages using YAML frontmatter at the top of the file.',
            'replace': '- Frontmatter tags MUST be provided for all pages using YAML frontmatter\n  at the top of the file.'
        },
        # Line 94 - Template instructions
        {
            'find': '- For all template entities, always reference standard attributes from the Base Entity (e.g., "This template entity includes',
            'replace': '- For all template entities, always reference standard attributes from the\n  Base Entity (e.g., "This template entity includes'
        },
        # Line 97-98 - Additional instructions
        {
            'find': '- For entities with additional attributes beyond Base Entity, list them clearly after the reference',
            'replace': '- For entities with additional attributes beyond Base Entity, list them\n  clearly after the reference'
        },
        {
            'find': '- Use bullet points for additional attributes to maintain clarity and easy scanning for users',
            'replace': '- Use bullet points for additional attributes to maintain clarity and easy\n  scanning for users'
        },
        # Line 112 - Modeling rules
        {
            'find': '- Use a data table format when showing entity structure relationships (like between value objects, entities, and domain services)',
            'replace': '- Use a data table format when showing entity structure relationships\n  (like between value objects, entities, and domain services)'
        },
        # Line 114 - Very long line
        {
            'find': 'standard attributes from the [Base Entity](../foundation/base_entity.md)")  (truncated…)',
            'replace': 'standard attributes from the\n    [Base Entity](../foundation/base_entity.md)")  (truncated…)'
        },
        # Line 118 - Writing style
        {
            'find': '- Write clear, action-oriented headers that explain what the reader will learn or accomplish',
            'replace': '- Write clear, action-oriented headers that explain what the reader will\n  learn or accomplish'
        },
        # Line 122 - Technical writing
        {
            'find': '- Technical writing should be precise and concise while remaining accessible to new team members',
            'replace': '- Technical writing should be precise and concise while remaining\n  accessible to new team members'
        }
    ]
    
    # Apply fixes
    for fix in fixes:
        if fix['find'] in content:
            content = content.replace(fix['find'], fix['replace'])
            print(f"Applied fix: {fix['find'][:50]}...")
        else:
            print(f"Fix not found: {fix['find'][:50]}...")
    
    # Additional regex-based fixes for remaining long lines
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        if len(line) > 80 and not line.strip().startswith('http') and not line.strip().startswith('|'):
            # Try to break at natural points for very long lines
            if ' - ' in line and len(line) > 120:
                # Split list items with descriptions
                parts = line.split(' - ', 1)
                if len(parts) == 2:
                    fixed_lines.append(parts[0] + ' -')
                    fixed_lines.append('  ' + parts[1])
                    continue
            elif ': ' in line and len(line) > 100:
                # Split at colon for definitions
                colon_pos = line.find(': ')
                if colon_pos > 0 and colon_pos < 60:
                    fixed_lines.append(line[:colon_pos + 1])
                    fixed_lines.append('  ' + line[colon_pos + 2:])
                    continue
            elif ', ' in line and len(line) > 100:
                # Split at comma for long sentences
                mid_point = 60
                comma_pos = line.find(', ', mid_point)
                if comma_pos > 0:
                    fixed_lines.append(line[:comma_pos + 1])
                    fixed_lines.append(line[comma_pos + 2:])
                    continue
        
        fixed_lines.append(line)
    
    # Write back the fixed content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))
    
    print(f"Fixed line length issues in {file_path}")

def main():
    print("=== Fixing remaining line length issues ===")
    fix_github_instructions_line_length()
    print("=== Line length fixes completed ===")

if __name__ == '__main__':
    main()
