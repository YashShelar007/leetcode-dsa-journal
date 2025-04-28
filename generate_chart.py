import os
import matplotlib.pyplot as plt

CATEGORY_TITLES = {
    "arrays_hashing": "Arrays & Hashing",
    "two_pointers": "Two Pointers",
    "sliding_window": "Sliding Window",
    "stack_queue": "Stacks & Queue",
    "binary_search": "Binary Search",
    "linked_list": "Linked List",
    "trees": "Trees",
    "graphs": "Graphs",
    "greedy": "Greedy",
    "backtracking": "Backtracking",
}

def count_problems_per_category():
    counts = {v: 0 for v in CATEGORY_TITLES.values()}
    for folder in CATEGORY_TITLES:
        if os.path.exists(folder):
            py_files = [f for f in os.listdir(folder) if f.endswith('.py')]
            counts[CATEGORY_TITLES[folder]] = len(py_files)
    return counts

def plot_chart(counts):
    categories = list(counts.keys())
    values = list(counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.barh(categories, values, color="orange")
    plt.xlabel("Problems Solved")
    plt.title("Problems Solved per Category")
    plt.tight_layout()
    plt.savefig("docs/chart.png")

if __name__ == "__main__":
    counts = count_problems_per_category()
    plot_chart(counts)
