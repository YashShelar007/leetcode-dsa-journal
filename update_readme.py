import os
import subprocess
import sys
import re

def get_changed_py_files() -> list[str]:
    # List .py files changed in the last commit
    out = subprocess.check_output(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        text=True
    )
    # return [f.strip() for f in out.splitlines() if f.strip().endswith(".py")]
    # Only include .py files inside a folder (i.e. "category/file.py"), not root scripts
    return [
        f.strip() for f in out.splitlines()
        if f.strip().endswith(".py") and "/" in f.strip()
    ]

def derive_entry(path: str) -> tuple[str,str,str]:
    """
    Given "two_pointers/valid_palindrome.py" returns
    ("Valid Palindrome", "Two Pointers", path).
    """
    folder, fname = path.split("/", 1)
    title = fname.replace(".py", "").replace("_", " ").title()
    category = folder.replace("_", " ").title()
    return title, category, path

def compute_next_day(readme_lines: list[str]) -> int:
    start = readme_lines.index("<!-- AUTO-GENERATED-TABLE-START -->")
    end   = readme_lines.index("<!-- AUTO-GENERATED-TABLE-END -->")

    # Match only lines that begin with "| Day " followed by a digit (e.g., "| Day 1", "| Day 12", etc.)
    day_rows = [
        line for line in readme_lines[start+1:end]
        if re.match(r"\|\s*Day\s+\d+", line.strip())
    ]

    return len(day_rows) + 1

def append_row_to_readme(entries: list[tuple[str,str,str]]):
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    day = compute_next_day(lines)
    # Build the markdown row
    titles = ", ".join(f"[{t}]({p})" for t,_,p in entries)
    cats   = " / ".join(sorted({c for _,c,_ in entries}))
    new_row = f"| Day {day} | {titles} | {cats} |"

    # Insert it just before the END marker
    out = []
    for line in lines:
        if line.strip() == "<!-- AUTO-GENERATED-TABLE-END -->":
            out.append(new_row)
        out.append(line)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

if __name__ == "__main__":
    changed = get_changed_py_files()
    if not changed:
        print("❌ No Python files changed in last commit, skipping README update.")
        sys.exit(0)

    entries = [derive_entry(p) for p in changed]
    append_row_to_readme(entries)
    print(f"✅ Appended Day row for {len(entries)} problem(s): {changed}")
