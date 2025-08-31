#!/usr/bin/env python3
"""
Comprehensive automated fix for all remaining markdownlint line length issues
"""

import re
import subprocess
from pathlib import Path

def get_line_length_errors():
    """Get all line length errors from markdownlint"""
    try:
        result = subprocess.run([
            'npx', 'markdownlint-cli2', 
            '--config', 'documents/.markdownlint-cli2.jsonc',
            '**/*.md', 
            '!.venv/**', 
            '!**/site/**', 
            '!**/node_modules/**'
        ], capture_output=True, text=True, shell=True)
        
        errors = []
        for line in result.stdout.split('\n'):
            if 'MD013/line-length' in line:
                # Parse error: file:line:col MD013/line-length ...
                parts = line.split(':')
                if len(parts) >= 3:
                    file_path = parts[0]
                    line_num = int(parts[1])
                    errors.append((file_path, line_num))
        
        return errors
    except Exception as e:
        print(f"Error getting line length errors: {e}")
        return []

def fix_line_length_in_file(file_path, line_num):
    """Fix a specific line length issue in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if line_num <= len(lines):
            line = lines[line_num - 1]
            original_line = line.rstrip()
            
            # Skip if line is not actually long
            if len(original_line) <= 80:
                return False
            
            # Skip lines that should not be broken
            if (original_line.strip().startswith('http') or 
                original_line.strip().startswith('|') or
                '```' in original_line or
                original_line.strip().startswith('#')):
                return False
            
            # Try different strategies to break the line
            fixed_line = None
            
            # Strategy 1: Break at natural sentence boundaries
            if '. ' in original_line:
                dot_pos = original_line.rfind('. ', 0, 75)
                if dot_pos > 30:
                    fixed_line = original_line[:dot_pos + 1] + '\n' + original_line[dot_pos + 2:]
            
            # Strategy 2: Break at commas
            elif ', ' in original_line:
                comma_pos = original_line.rfind(', ', 0, 75)
                if comma_pos > 30:
                    fixed_line = original_line[:comma_pos + 1] + '\n' + original_line[comma_pos + 2:]
            
            # Strategy 3: Break at 'and' or 'or'
            elif ' and ' in original_line:
                and_pos = original_line.rfind(' and ', 0, 75)
                if and_pos > 30:
                    fixed_line = original_line[:and_pos] + '\n' + original_line[and_pos + 1:]
            
            # Strategy 4: Break at parentheses
            elif '(' in original_line:
                paren_pos = original_line.rfind('(', 0, 75)
                if paren_pos > 30:
                    fixed_line = original_line[:paren_pos] + '\n' + original_line[paren_pos:]
            
            # Strategy 5: Break at spaces (last resort)
            elif ' ' in original_line:
                space_pos = original_line.rfind(' ', 0, 78)
                if space_pos > 30:
                    fixed_line = original_line[:space_pos] + '\n' + original_line[space_pos + 1:]
            
            if fixed_line:
                lines[line_num - 1] = fixed_line.rstrip() + '\n'
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                print(f"Fixed line {line_num} in {file_path}")
                return True
            
    except Exception as e:
        print(f"Error fixing {file_path}:{line_num}: {e}")
    
    return False

def main():
    print("=== Comprehensive Line Length Fix ===")
    
    # Get all line length errors
    errors = get_line_length_errors()
    print(f"Found {len(errors)} line length errors")
    
    if not errors:
        print("No line length errors found!")
        return
    
    # Fix each error
    fixed_count = 0
    for file_path, line_num in errors:
        if fix_line_length_in_file(file_path, line_num):
            fixed_count += 1
    
    print(f"Fixed {fixed_count} out of {len(errors)} line length issues")
    
    # Check remaining errors
    remaining_errors = get_line_length_errors()
    print(f"Remaining line length errors: {len(remaining_errors)}")
    
    if remaining_errors:
        print("\nRemaining errors:")
        for file_path, line_num in remaining_errors[:10]:  # Show first 10
            print(f"  {file_path}:{line_num}")

if __name__ == '__main__':
    main()
