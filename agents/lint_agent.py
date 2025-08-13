import re
from typing import Dict, List

# only scan ADDED lines in the diff, which start with "+"
def run_static_checks(pr_ctx: Dict) -> List[Dict]:
    findings: List[Dict] = []

    for f in pr_ctx["files"]:
        path = f["path"]
        diff = f["diff"]

        for line in diff.splitlines():
            if not line.startswith("+"):
                continue  

            code = line[1:]  # strip "+"

            # "except:" but not "except Exception:"
            if "except:" in code and "Exception" not in code:
                findings.append({
                    "file": path,
                    "type": "bare-except",
                    "line": line,
                    "msg": "Bare except detected. Catch a specific exception and re-raise."
                })

            if re.search(r"\bprint\(", code) and not path.endswith("_script.py"):
                findings.append({
                    "file": path,
                    "type": "print-in-lib",
                    "line": line,
                    "msg": "print found in library code. Prefer logging."
                })

            if len(code) > 120:
                findings.append({
                    "file": path,
                    "type": "long-line",
                    "line": line,
                    "msg": "Line exceeds 120 chars."
                })

    return findings

# Later we add AI based linting here
