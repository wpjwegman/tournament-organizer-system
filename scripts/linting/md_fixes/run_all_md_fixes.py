#!/usr/bin/env python3
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
        "fix_md005.py",
        "fix_md007.py",
        "fix_md010.py",
        "fix_md034.py",
        "fix_md049.py",
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


if __name__ == "__main__":
    sys.exit(main())
