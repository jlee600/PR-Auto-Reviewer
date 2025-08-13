from typing import Dict, List

def propose_patches(pr_ctx: Dict, findings: List[Dict]) -> List[Dict]:
    # Turn simple findings into tiny unified diff patches.
    
    suggestions: List[Dict] = []

    for fd in findings:
        file = fd["file"]
        ftype = fd["type"]

        if ftype == "bare-except":
            # Replace 'except:' with a specific catch and re-raise
            patch = f"""--- a/{file}
                +++ b/{file}
                @@
                -    except:
                +    except Exception as e:
                +        raise
                """
            suggestions.append({
                "kind": "patch",
                "file": file,
                "line_delta": 2,
                "risk": "low",
                "rationale": "Avoid bare except. Catch a specific exception and re-raise.",
                "content": patch,
            })

        elif ftype == "print-in-lib":
            # Replace print with logging
            patch = f"""--- a/{file}
                +++ b/{file}
                @@
                -    print(
                +    import logging
                +    logging.getLogger(__name__).info(
                """
            suggestions.append({
                "kind": "patch",
                "file": file,
                "line_delta": 1,
                "risk": "low",
                "rationale": "Prefer logging in library code.",
                "content": patch,
            })

        elif ftype == "long-line":
            patch = f"""--- a/{file}
                +++ b/{file}
                @@
                -<long line here>
                +<split the long line into shorter parts>
                """
            suggestions.append({
                "kind": "patch",
                "file": file,
                "line_delta": 0,
                "risk": "low",
                "rationale": "Break long lines to improve readability.",
                "content": patch,
            })

    return suggestions