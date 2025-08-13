'''
diff --git a/oldpath b/newpath
index <hash>..<hash> <mode>
--- a/file.py
+++ b/file.py
@@
+added line
-removed line
'''

from typing import List, Dict

def load_diff_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def parse_unified_diff(diff_text: str) -> List[Dict]:
    parts = diff_text.split("\ndiff --git ")
    files = []
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # First line after the split is the "diff --git a/... b/..." header
        header = "diff --git " + part.splitlines()[0]
        body = "\n".join(part.splitlines()[1:])

        old_path = None
        new_path = None
        for line in body.splitlines():
            if line.startswith("--- "):
                old_path = line[4:].strip()  # like "a/file.py"
            if line.startswith("+++ "):
                new_path = line[4:].strip()  # like "b/file.py"

        # Prefer the "b/" path since it points at the new file
        if new_path and new_path.startswith("b/"):
            path = new_path[2:]            # "file.py"
        elif old_path and old_path.startswith("a/"):
            path = old_path[2:]
        else:
            path = new_path or old_path or "unknown"

        files.append({"path": path, "header": header, "diff": body})
    return files
