import os
from datetime import datetime

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
    for folder in CATEGORY_TITLES:
        if not os.path.exists(folder):
            os.makedirs(folder)

def collect_problems():
    problems = []
    for category in os.listdir():
        if os.path.isdir(category) and category != '.git':
            if category in CATEGORY_TITLES:
                files = [f for f in os.listdir(category) if f.endswith('.py')]
                for file in sorted(files):
                    title = file.replace('_', ' ').replace('.py', '').title()
                    link = f"{category}/{file}"
                    problems.append((title, CATEGORY_TITLES[category], link))
    return problems

def generate_table(problems):
    table = "| Day | Problems Solved | Category |\n|-----|------------------|----------|\n"
    for i in range(0, len(problems), 2):
        p1 = problems[i]
        p2 = problems[i + 1] if i + 1 < len(problems) else None
        titles = f"[{p1[0]}]({p1[2]})"
        if p2:
            titles += f", [{p2[0]}]({p2[2]})"
        category = p1[1] if p1[1] == (p2[1] if p2 else p1[1]) else f"{p1[1]} / {p2[1]}" if p2 else p1[1]
        table += f"| Day {(i // 2) + 1} | {titles} | {category} |\n"
    return table

def update_readme():
    ensure_folder_structure()
    with open("README.md", "r") as f:
        content = f.read()

    problems = collect_problems()
    table = generate_table(problems)

    start = "<!-- AUTO-GENERATED-TABLE-START -->"
    end = "<!-- AUTO-GENERATED-TABLE-END -->"
    updated_content = f"{start}\n{table}{end}"

    new_readme = content.split(start)[0] + updated_content + content.split(end)[1]

    with open("README.md", "w") as f:
        f.write(new_readme)

    print("✅ README.md updated successfully.")

if __name__ == "__main__":
    update_readme()
