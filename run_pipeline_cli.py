import argparse, os

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--diff-file", required=True, help="path to a unified diff file")
    args = p.parse_args()

    os.makedirs("out", exist_ok=True)

    with open("out/report.md", "w", encoding="utf-8") as f:
        f.write("# Report\n\n")
        f.write(f"Loaded diff from: {args.diff_file}\n")

    print("wrote out/report.md")

if __name__ == "__main__":
    main()