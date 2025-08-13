# Report

Files changed: ['example.py']
- example.py functions: ['add', 'extra']

Findings:
- print-in-lib in example.py: print found in library code. Prefer logging.
- bare-except in example.py: Bare except detected. Catch a specific exception and re-raise.

Patch suggestions:

[example.py] Prefer logging in library code.
```diff
--- a/example.py
                +++ b/example.py
                @@
                -    print(
                +    import logging
                +    logging.getLogger(__name__).info(
                ```

[example.py] Avoid bare except. Catch a specific exception and re-raise.
```diff
--- a/example.py
                +++ b/example.py
                @@
                -    except:
                +    except Exception as e:
                +        raise
                ```
