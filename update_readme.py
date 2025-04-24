import os

# Map folder names to human-readable categories
CATEGORY_TITLES = {
    "arrays_hashing": "Arrays & Hashing",
    "two_pointers": "Two Pointers",
    "sliding_window": "Sliding Window",
    "stack": "Stack",
    "binary_search": "Binary Search",
    "linked_list": "Linked List",
    "trees": "Trees",
    "graphs": "Graphs",
    "greedy": "Greedy",
    "backtracking": "Backtracking",
}

def ensure_folder_structure():
    """Make sure each category folder exists (so chart/counts don’t break)."""
    repo_root = os.path.dirname(os.path.abspath(__file__))
    for folder in CATEGORY_TITLES:
        path = os.path.join(repo_root, folder)
        if not os.path.exists(path):
            os.makedirs(path)

def collect_problems():
    """
    Walk through each known category folder and collect
    (title, category, link) tuples for every .py file.
    """
    repo_root = os.path.dirname(os.path.abspath(__file__))
    problems = []

    for folder, category in CATEGORY_TITLES.items():
        folder_path = os.path.join(repo_root, folder)
        if os.path.isdir(folder_path):
            for file in sorted(os.listdir(folder_path)):
                if file.endswith(".py"):
                    # Turn "two_sum.py" → "Two Sum"
                    title = file.replace("_", " ").replace(".py", "").title()
                    link = f"{folder}/{file}"
                    problems.append((title, category, link))

    return problems

def generate_table(problems):
    """
    Build the Markdown table string. Groups every two problems into one row.
    """
    header = "| Day | Problems Solved | Category |\n|-----|------------------|----------|\n"
    rows = []
    for i in range(0, len(problems), 2):
        p1 = problems[i]
        p2 = problems[i+1] if i+1 < len(problems) else None

        titles = f"[{p1[0]}]({p1[2]})"
        if p2:
            titles += f", [{p2[0]}]({p2[2]})"

        if p2 and p1[1] != p2[1]:
            category = f"{p1[1]} / {p2[1]}"
        else:
            category = p1[1]

        day = (i // 2) + 1
        rows.append(f"| Day {day} | {titles} | {category} |")

    return header + "\n".join(rows) + "\n"

def update_readme():
    """Read README.md, replace the table, and write it back out."""
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
