import argparse, os
from utils.diff_utils import load_diff_from_file, parse_unified_diff
from agents.context_agent import build_context

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--diff-file", required=True, help="path to a unified diff file")
    args = p.parse_args()

    text = load_diff_from_file(args.diff_file)
    files = parse_unified_diff(text)
    ctx = build_context(files)

    os.makedirs("out", exist_ok=True)

    with open("out/report.md", "w", encoding="utf-8") as f:
        f.write("# Report\n\n")
        f.write(f"Files changed: {[f['path'] for f in files]}\n")
        for fi in ctx["files"]:
            f.write(f"- {fi['path']} functions: {fi['functions']}\n")

    print(f"parsed {len(files)} file(s). wrote out/report.md")

if __name__ == "__main__":
    main()