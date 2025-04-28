import os
from collections import OrderedDict

# ———— Define the exact folder order you solve in — no surprises ————
CATEGORY_TITLES = OrderedDict([
    ("arrays_hashing", "Arrays & Hashing"),
    ("two_pointers",    "Two Pointers"),
    ("sliding_window",  "Sliding Window"),
    ("binary_search",   "Binary Search"),
    ("matrix",          "Matrix"),             # your search-a-2d-matrix-ii folder
    ("linked_list",     "Linked List"),
    ("trees",           "Trees"),
    ("graphs",          "Graphs"),
    ("greedy",          "Greedy"),
    ("backtracking",    "Backtracking"),
    ("stack_queue", "Stacks & Queue")
])

def collect_problems():
    """
    Walk through each category in the exact solve order,
    collect all .py files (if any), and build (title, category, link).
    """
    repo_root = os.path.dirname(os.path.abspath(__file__))
    problems = []

    for folder, label in CATEGORY_TITLES.items():
        folder_path = os.path.join(repo_root, folder)
        if not os.path.isdir(folder_path):
            continue  # you haven’t created this category yet

        py_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".py")])
        if not py_files:
            continue  # you solved no problems in this category yet

        for fname in py_files:
            title = fname.replace("_", " ").replace(".py", "").title()
            link  = f"{folder}/{fname}"
            problems.append((title, label, link))

    return problems

def generate_table(problems):
    """
    Build Markdown table two problems per day in the order they were appended.
    """
    header = "| Day | Problems Solved | Category |\n|-----|------------------|----------|\n"
    rows = []
    for i in range(0, len(problems), 2):
        p1 = problems[i]
        p2 = problems[i+1] if i+1 < len(problems) else None

        titles = f"[{p1[0]}]({p1[2]})"
        if p2:
            titles += f", [{p2[0]}]({p2[2]})"

        # merge categories for the row, or show single if same
        if p2 and p1[1] != p2[1]:
            cat = f"{p1[1]} / {p2[1]}"
        else:
            cat = p1[1]

        day = (i // 2) + 1
        rows.append(f"| Day {day} | {titles} | {cat} |")

    return header + "\n".join(rows) + "\n"

def update_readme():
    repo_root  = os.path.dirname(os.path.abspath(__file__))
    readme_md  = os.path.join(repo_root, "README.md")

    with open(readme_md, "r", encoding="utf-8") as f:
        content = f.read()

    problems = collect_problems()
    table_md = generate_table(problems)

    start_tag = "<!-- AUTO-GENERATED-TABLE-START -->"
    end_tag   = "<!-- AUTO-GENERATED-TABLE-END -->"

    before = content.split(start_tag)[0]
    after  = content.split(end_tag)[1] if end_tag in content else ""

    new_content = before + start_tag + "\n" + table_md + end_tag + after
    with open(readme_md, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ README.md updated successfully.")

if __name__ == "__main__":
    update_readme()
