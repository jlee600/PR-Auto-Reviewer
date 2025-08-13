# Report

Files changed: ['example.py']
- example.py functions: ['add', 'extra']

Findings:
- print-in-lib in example.py: print found in library code. Prefer logging.
- bare-except in example.py: Bare except detected. Catch a specific exception and re-raise.
