#!/usr/bin/env python3
"""
Enterprise Markdown Error Analysis Tool

Analyzes markdownlint-cli2 output to categorize errors and generate fix plans.
Part of the professional automation suite for enterprise documentation quality.
"""
import subprocess
import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

class MarkdownErrorAnalyzer:
    def __init__(self, domains: List[str]):
        self.domains = domains
        self.error_summary = defaultdict(lambda: defaultdict(list))
        self.fix_plan = defaultdict(list)
        
    def analyze_domain(self, domain: str) -> Dict[str, List[str]]:
        """Analyze a single domain for markdown errors."""
        try:
            result = subprocess.run([
                "markdownlint-cli2", 
                f"documents/docs/domains/{domain}/**/*.md"
            ], 
            capture_output=True, 
            text=True
            )
            
            errors = {}
            if result.returncode != 0 and result.stdout:
                for line in result.stdout.strip().split('\n'):
                    if ':' in line and ('MD' in line or 'error' in line.lower()):
                        # Parse: file:line:col error_code/rule_name Description
                        parts = line.split(':', 3)
                        if len(parts) >= 3:
                            file_path = parts[0]
                            line_num = parts[1]
                            col_num = parts[2] if len(parts) > 2 else ''
                            error_detail = parts[3] if len(parts) > 3 else ''
                            
                            # Extract error code (MD###)
                            error_code = re.search(r'(MD\d+)', error_detail)
                            error_code = error_code.group(1) if error_code else 'UNKNOWN'
                            
                            if file_path not in errors:
                                errors[file_path] = []
                            errors[file_path].append({
                                'line': line_num,
                                'column': col_num,
                                'code': error_code,
                                'detail': error_detail.strip()
                            })
            
            return errors
            
        except Exception as e:
            print(f"Error analyzing domain {domain}: {e}")
            return {}
    
    def analyze_all_domains(self) -> Dict[str, Dict[str, int]]:
        """Analyze all domains and categorize errors."""
        total_summary = defaultdict(int)
        
        for domain in self.domains:
            print(f"🔍 Analyzing {domain} domain...")
            errors = self.analyze_domain(domain)
            
            domain_summary = defaultdict(int)
            for file_path, file_errors in errors.items():
                for error in file_errors:
                    error_code = error['code']
                    domain_summary[error_code] += 1
                    total_summary[error_code] += 1
                    
                    # Store for detailed fix planning
                    self.error_summary[domain][error_code].append({
                        'file': file_path,
                        'line': error['line'],
                        'column': error['column'],
                        'detail': error['detail']
                    })
            
            if domain_summary:
                print(f"  📊 {domain}: {dict(domain_summary)}")
            else:
                print(f"  ✅ {domain}: Clean")
        
        return dict(total_summary)
    
    def generate_fix_plan(self, error_summary: Dict[str, int]) -> Dict[str, Dict]:
        """Generate automated fix plan based on error analysis."""
        fix_plan = {}
        
        # MD010: Hard tabs - Easy automation
        if 'MD010' in error_summary:
            fix_plan['MD010'] = {
                'priority': 'HIGH',
                'automation': 'FULL',
                'method': 'find_replace',
                'description': 'Replace hard tabs with spaces',
                'script_needed': True
            }
        
        # MD007: List indentation - Custom fixer exists
        if 'MD007' in error_summary:
            fix_plan['MD007'] = {
                'priority': 'HIGH',
                'automation': 'FULL',
                'method': 'existing_fixer',
                'description': 'Use existing fix_md007.py script',
                'script_needed': False
            }
        
        # MD005: Inconsistent list indentation - Custom automation
        if 'MD005' in error_summary:
            fix_plan['MD005'] = {
                'priority': 'HIGH',
                'automation': 'FULL',
                'method': 'list_standardization',
                'description': 'Standardize list indentation',
                'script_needed': True
            }
        
        # MD034: Bare URLs - Pattern replacement
        if 'MD034' in error_summary:
            fix_plan['MD034'] = {
                'priority': 'MEDIUM',
                'automation': 'SEMI',
                'method': 'url_wrapping',
                'description': 'Wrap bare URLs in markdown link syntax',
                'script_needed': True
            }
        
        # MD049: Emphasis style - Pattern replacement
        if 'MD049' in error_summary:
            fix_plan['MD049'] = {
                'priority': 'MEDIUM',
                'automation': 'FULL',
                'method': 'emphasis_standardization',
                'description': 'Convert underscore emphasis to asterisk',
                'script_needed': True
            }
        
        # MD033: Inline HTML - Manual review needed
        if 'MD033' in error_summary:
            fix_plan['MD033'] = {
                'priority': 'LOW',
                'automation': 'MANUAL',
                'method': 'review_required',
                'description': 'Review inline HTML elements for necessity',
                'script_needed': False
            }
        
        return fix_plan
    
    def print_analysis_report(self, error_summary: Dict[str, int], fix_plan: Dict[str, Dict]):
        """Print comprehensive analysis report."""
        print("\n" + "="*80)
        print("📊 ENTERPRISE MARKDOWN ERROR ANALYSIS REPORT")
        print("="*80)
        
        print(f"\n🎯 SUMMARY:")
        print(f"   Total Error Types: {len(error_summary)}")
        print(f"   Total Errors: {sum(error_summary.values())}")
        print(f"   Domains Analyzed: {len(self.domains)}")
        
        print(f"\n📈 ERROR BREAKDOWN:")
        for error_code, count in sorted(error_summary.items()):
            automation_level = fix_plan.get(error_code, {}).get('automation', 'UNKNOWN')
            priority = fix_plan.get(error_code, {}).get('priority', 'UNKNOWN')
            print(f"   {error_code}: {count} occurrences ({automation_level} automation, {priority} priority)")
        
        print(f"\n🔧 AUTOMATION FEASIBILITY:")
        full_auto = sum(1 for plan in fix_plan.values() if plan.get('automation') == 'FULL')
        semi_auto = sum(1 for plan in fix_plan.values() if plan.get('automation') == 'SEMI')
        manual = sum(1 for plan in fix_plan.values() if plan.get('automation') == 'MANUAL')
        
        print(f"   Full Automation: {full_auto} error types")
        print(f"   Semi Automation: {semi_auto} error types")
        print(f"   Manual Review: {manual} error types")
        
        total_auto_errors = sum(count for code, count in error_summary.items() 
                               if fix_plan.get(code, {}).get('automation') in ['FULL', 'SEMI'])
        automation_percentage = (total_auto_errors / sum(error_summary.values())) * 100
        print(f"   Automation Coverage: {automation_percentage:.1f}%")

def main():
    domains = ['classification', 'code_of_conduct', 'communication', 'discipline', 
               'finance', 'first_aid', 'foundation', 'identity']
    
    analyzer = MarkdownErrorAnalyzer(domains)
    error_summary = analyzer.analyze_all_domains()
    fix_plan = analyzer.generate_fix_plan(error_summary)
    analyzer.print_analysis_report(error_summary, fix_plan)
    
    return analyzer, error_summary, fix_plan

if __name__ == "__main__":
    analyzer, errors, plan = main()
