#!/usr/bin/env python3
"""
MD005 Fixer: Inconsistent List Indentation

Standardizes list indentation for consistent markdown formatting.
Part of the enterprise automation suite.
"""
import sys
import re

def fix_md005(file_path):
    """Fix MD005: Standardize list indentation."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    in_list = False
    list_level = 0
    
    for line in lines:
        # Check if this is a list item
        list_match = re.match(r'^(\s*)([-*+])\s+(.*)', line)
        if list_match:
            indent, bullet, content = list_match.groups()
            current_level = len(indent) // 2
            
            # Standardize indentation: 0 spaces for level 0, 2 spaces per level
            standard_indent = '  ' * current_level
            fixed_line = f'{standard_indent}{bullet} {content}\n'
            fixed_lines.append(fixed_line)
            in_list = True
        else:
            fixed_lines.append(line)
            # Reset list tracking if we hit a non-list line
            if line.strip() and not line.startswith(' ') and in_list:
                in_list = False
    
    fixed_content = ''.join(fixed_lines)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    if fixed_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"[MD005] Fixed inconsistent list indentation in {file_path}")
        return True
    return False

def main():
    files = sys.argv[1:]
    fixed_count = 0
    for file_path in files:
        if fix_md005(file_path):
            fixed_count += 1
    
    if fixed_count > 0:
        print(f"[MD005] Fixed {fixed_count} files with inconsistent list indentation")
    else:
        print("[MD005] No inconsistent list indentation found")

if __name__ == "__main__":
    main()
