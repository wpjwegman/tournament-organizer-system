#!/usr/bin/env python3
"""
Comprehensive fix for remaining CI/CD issues identified from GitHub Actions logs
"""

import os
import re
import glob
import subprocess
from pathlib import Path


def fix_markdownlint_errors():
    """Fix specific markdownlint errors found in logs"""
    fixes = [
        # Fix backend/README.md line length issues
        {
            'file': 'backend/README.md',
            'line': 3,
            'find': 'This backend API will provide RESTful endpoints for the tournament organizer system.',
            'replace': 'This backend API will provide RESTful endpoints for the tournament\norganizer system.'
        },
        {
            'file': 'backend/README.md', 
            'line': 34,
            'find': 'Future implementation will include database models and API endpoint definitions.',
            'replace': 'Future implementation will include database models and API endpoint\ndefinitions.'
        },
        
        # Fix DOCUMENTATION_QUALITY.md issues
        {
            'file': 'DOCUMENTATION_QUALITY.md',
            'line': 5,
            'find': 'This document establishes clear standards for documentation quality across all domains in the Tournament Organizer System, ensuring consistency and maintainability.',
            'replace': 'This document establishes clear standards for documentation quality\nacross all domains in the Tournament Organizer System, ensuring\nconsistency and maintainability.'
        },
        {
            'file': 'DOCUMENTATION_QUALITY.md',
            'line': 274,
            'find': 'All validation checks must pass before PR approval, including automated linting, manual review of content accuracy, and verification of links.',
            'replace': 'All validation checks must pass before PR approval, including automated\nlinting, manual review of content accuracy, and verification of links.'
        },
        
        # Fix scripts/README.md issues
        {
            'file': 'scripts/README.md',
            'line': 15,
            'find': 'You can validate documentation locally by running: `./scripts/validate-docs.ps1`',
            'replace': 'You can validate documentation locally by running:\n`./scripts/validate-docs.ps1`'
        },
        {
            'file': 'scripts/README.md',
            'line': 52,
            'find': 'These scripts are designed to work cross-platform and maintain consistency across different development environments while ensuring high documentation quality.',
            'replace': 'These scripts are designed to work cross-platform and maintain\nconsistency across different development environments while ensuring high\ndocumentation quality.'
        }
    ]
    
    for fix in fixes:
        file_path = Path(fix['file'])
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Apply the fix
                if fix['find'] in content:
                    content = content.replace(fix['find'], fix['replace'])
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed line length in {fix['file']}")
                else:
                    print(f"Text not found in {fix['file']}: {fix['find'][:50]}...")
            except Exception as e:
                print(f"Error fixing {fix['file']}: {e}")


def fix_list_spacing_issues():
    """Fix MD032 blanks-around-lists issues"""
    files_to_fix = [
        'DOCUMENTATION_QUALITY.md',
        '.github/WORKFLOW_INTEGRATION.md'
    ]
    
    for file_path in files_to_fix:
        if Path(file_path).exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                fixed_lines = []
                for i, line in enumerate(lines):
                    # Add blank line before numbered lists
                    if re.match(r'^\d+\.', line.strip()) and i > 0:
                        prev_line = lines[i-1].strip()
                        if prev_line and not prev_line.endswith(':') and not re.match(r'^\d+\.', prev_line):
                            fixed_lines.append('\n')
                    
                    fixed_lines.append(line)
                    
                    # Add blank line after lists
                    if re.match(r'^\d+\.', line.strip()) and i < len(lines) - 1:
                        next_line = lines[i+1].strip()
                        if next_line and not re.match(r'^\d+\.', next_line) and not next_line.startswith('   '):
                            fixed_lines.append('\n')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(fixed_lines)
                print(f"Fixed list spacing in {file_path}")
            except Exception as e:
                print(f"Error fixing list spacing in {file_path}: {e}")


def fix_github_instructions():
    """Fix GitHub instructions files formatting"""
    instruction_files = glob.glob('.github/instructions/*.md')
    
    for file_path in instruction_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix unordered list indentation (MD007)
            lines = content.split('\n')
            fixed_lines = []
            
            for line in lines:
                if line.startswith('  -') or line.startswith('  *'):
                    # Fix 2-space indentation to 0
                    fixed_lines.append(line[2:])
                elif line.startswith('    -') or line.startswith('    *'):
                    # Fix 4-space indentation to 2
                    fixed_lines.append('  ' + line[4:])
                elif line.startswith('      -') or line.startswith('      *'):
                    # Fix 6-space indentation to 4
                    fixed_lines.append('    ' + line[6:])
                else:
                    fixed_lines.append(line)
            
            # Fix line length issues (MD013) - break long lines
            final_lines = []
            for line in fixed_lines:
                if len(line) > 80 and not line.strip().startswith('http'):
                    # Try to break at natural points
                    if ' - ' in line:
                        parts = line.split(' - ', 1)
                        if len(parts) == 2:
                            final_lines.append(parts[0] + ' -')
                            final_lines.append('  ' + parts[1])
                            continue
                    elif ', ' in line and len(line) > 100:
                        # Break at comma for very long lines
                        mid_point = len(line) // 2
                        comma_pos = line.find(', ', mid_point)
                        if comma_pos > 0:
                            final_lines.append(line[:comma_pos + 1])
                            final_lines.append(line[comma_pos + 2:])
                            continue
                
                final_lines.append(line)
            
            # Fix fenced code blocks (MD040)
            content = '\n'.join(final_lines)
            content = re.sub(r'^```$', '```markdown', content, flags=re.MULTILINE)
            
            # Fix heading indentation (MD023)
            content = re.sub(r'^  (#{1,6}) ', r'\1 ', content, flags=re.MULTILINE)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed GitHub instructions: {file_path}")
        except Exception as e:
            print(f"Error fixing {file_path}: {e}")


def fix_issue_template():
    """Fix GitHub issue template"""
    template_path = '.github/ISSUE_TEMPLATE/domain-quality-update.md'
    if Path(template_path).exists():
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix MD022 - headings surrounded by blank lines
            lines = content.split('\n')
            fixed_lines = []
            
            for i, line in enumerate(lines):
                if line.startswith('#'):
                    # Add blank line before heading if not at start and previous line isn't blank
                    if i > 0 and lines[i-1].strip():
                        fixed_lines.append('')
                    fixed_lines.append(line)
                    # Add blank line after heading if next line isn't blank
                    if i < len(lines) - 1 and lines[i+1].strip():
                        fixed_lines.append('')
                else:
                    fixed_lines.append(line)
            
            # Fix MD025 - remove duplicate H1s (keep only the first one)
            content = '\n'.join(fixed_lines)
            h1_pattern = r'^# .*$'
            h1_matches = list(re.finditer(h1_pattern, content, re.MULTILINE))
            
            if len(h1_matches) > 1:
                # Replace subsequent H1s with H2s
                for match in h1_matches[1:]:
                    content = content[:match.start()] + '##' + content[match.start()+1:]
            
            # Fix line length issues
            lines = content.split('\n')
            final_lines = []
            for line in lines:
                if len(line) > 80 and not line.strip().startswith('http'):
                    words = line.split()
                    current_line = ''
                    for word in words:
                        if len(current_line + ' ' + word) <= 80:
                            current_line += (' ' + word) if current_line else word
                        else:
                            if current_line:
                                final_lines.append(current_line)
                            current_line = word
                    if current_line:
                        final_lines.append(current_line)
                else:
                    final_lines.append(line)
            
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(final_lines))
            
            print(f"Fixed issue template: {template_path}")
        except Exception as e:
            print(f"Error fixing issue template: {e}")


def fix_readme_multiple_blanks():
    """Fix MD012 multiple consecutive blank lines in README.md"""
    if Path('README.md').exists():
        try:
            with open('README.md', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace multiple consecutive blank lines with single blank line
            content = re.sub(r'\n{3,}', '\n\n', content)
            
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("Fixed multiple blank lines in README.md")
        except Exception as e:
            print(f"Error fixing README.md: {e}")


def fix_python_unused_variables():
    """Fix Python unused variables found by ruff"""
    fixes = [
        {
            'file': 'documents/fix_markdownlint_errors.py',
            'line': 55,
            'remove': '            in_table = False'
        },
        {
            'file': 'documents/scripts/linting/md_fixes/fix_md005.py',
            'line': 37,
            'remove': '                list_level = 0'
        }
    ]
    
    for fix in fixes:
        file_path = Path(fix['file'])
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Remove the specified line
                if fix['line'] <= len(lines):
                    line_content = lines[fix['line'] - 1].strip()
                    if fix['remove'].strip() in line_content:
                        lines.pop(fix['line'] - 1)
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        print(f"Removed unused variable from {fix['file']}")
            except Exception as e:
                print(f"Error fixing Python file {fix['file']}: {e}")


def fix_missing_script_file():
    """Create missing script file referenced in pre-commit config"""
    missing_script = Path('scripts/linting/md_fixes/run_all_md_fixes.py')
    
    if not missing_script.exists():
        missing_script.parent.mkdir(parents=True, exist_ok=True)
        
        script_content = '''#!/usr/bin/env python3
"""
Run all markdown fixes for domain linting
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Run all markdown fixes"""
    fixes_dir = Path(__file__).parent
    
    # List of fix scripts to run
    fix_scripts = [
        'fix_md005.py',
        'fix_md007.py', 
        'fix_md010.py',
        'fix_md034.py',
        'fix_md049.py'
    ]
    
    for script in fix_scripts:
        script_path = fixes_dir / script
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
                print(f"Executed {script}")
            except subprocess.CalledProcessError as e:
                print(f"Error running {script}: {e}")
                return 1
        else:
            print(f"Warning: {script} not found")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
'''
        
        with open(missing_script, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        print(f"Created missing script: {missing_script}")


def main():
    """Run all fixes"""
    print("=== Fixing remaining CI/CD issues ===")
    
    # Change to the repository root
    repo_root = Path(__file__).parent
    os.chdir(repo_root)
    
    print("\n1. Fixing markdownlint line length errors...")
    fix_markdownlint_errors()
    
    print("\n2. Fixing list spacing issues...")
    fix_list_spacing_issues()
    
    print("\n3. Fixing GitHub instructions formatting...")
    fix_github_instructions()
    
    print("\n4. Fixing issue template...")
    fix_issue_template()
    
    print("\n5. Fixing README multiple blank lines...")
    fix_readme_multiple_blanks()
    
    print("\n6. Fixing Python unused variables...")
    fix_python_unused_variables()
    
    print("\n7. Creating missing script file...")
    fix_missing_script_file()
    
    print("\n=== All fixes completed ===")
    print("\nNext steps:")
    print("1. Run the script locally")
    print("2. Commit and push changes")
    print("3. Monitor GitHub Actions for success")


if __name__ == '__main__':
    main()
