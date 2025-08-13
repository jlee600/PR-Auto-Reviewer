import re
from typing import List

# +def 
DEF_LINE = re.compile(r'^\+def\s+([a-zA-Z_]\w*)\s*\(', re.M)

def find_changed_functions(diff_chunk: str) -> List[str]:
    names = set(m.group(1) for m in DEF_LINE.finditer(diff_chunk))
    return sorted(names)