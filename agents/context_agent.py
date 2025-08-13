from typing import Dict, List
from utils.text import find_changed_functions

def build_context(files: List[Dict]) -> Dict:
    ctx_files = []
    for f in files:
        funcs = find_changed_functions(f["diff"])
        ctx_files.append({
            "path": f["path"],
            "diff": f["diff"],
            "functions": funcs
        })
    return {"files": ctx_files}