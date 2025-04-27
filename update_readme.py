import os

# Folders to ignore when scanning for problem categories
IGNORED_DIRS = {".github", "docs", "__pycache__",}

def ensure_folder_structure():
    """
    Create any category folders you expect to use.
    (You can still add new ones manually without touching this script.)
    """
    # If you want a template set of folders, list them here.
    for folder in []:
        if not os.path.exists(folder):
            os.makedirs(folder)

def collect_problems():
    """
    Walk through each top-level directory (except IGNORED_DIRS),
    collect all .py files, and assign a human-friendly category.
    """
    repo_root = os.path.dirname(os.path.abspath(__file__))
    problems = []

    for entry in sorted(os.listdir(repo_root)):
        full_path = os.path.join(repo_root, entry)
        if not os.path.isdir(full_path) or entry in IGNORED_DIRS:
            continue

        # Derive category name from folder, e.g. "two_pointers" → "Two Pointers"
        category = entry.replace("_", " ").title()

        # Add each Python file in this folder
        for fname in sorted(os.listdir(full_path)):
            if fname.endswith(".py"):
                title = fname.replace("_", " ").replace(".py", "").title()
                link  = f"{entry}/{fname}"
                problems.append((title, category, link))

    return problems

def generate_table(problems):
    """
    Build the Markdown table: two problems per day, in chronological order.
    """
    header = "| Day | Problems Solved | Category |\n|-----|------------------|----------|\n"
    rows = []
    for i in range(0, len(problems), 2):
        p1 = problems[i]
        p2 = problems[i+1] if i+1 < len(problems) else None

        titles = f"[{p1[0]}]({p1[2]})"
        if p2:
            titles += f", [{p2[0]}]({p2[2]})"

        # If both problems share a category, show it once; otherwise join with " / "
        if p2 and p1[1] != p2[1]:
            cat = f"{p1[1]} / {p2[1]}"
        else:
            cat = p1[1]

        day = (i // 2) + 1
        rows.append(f"| Day {day} | {titles} | {cat} |")

    return header + "\n".join(rows) + "\n"

def update_readme():
    """
    Read README.md, replace the auto-table section, and write back.
    """
    repo_root = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(repo_root, "README.md")

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    problems = collect_problems()
    table_md = generate_table(problems)

    start_tag = "<!-- AUTO-GENERATED-TABLE-START -->"
    end_tag   = "<!-- AUTO-GENERATED-TABLE-END -->"

    before = content.split(start_tag)[0]
    after  = content.split(end_tag)[1] if end_tag in content else ""

    new_content = before + start_tag + "\n" + table_md + end_tag + after

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ README.md updated successfully.")

if __name__ == "__main__":
    ensure_folder_structure()
    update_readme()
