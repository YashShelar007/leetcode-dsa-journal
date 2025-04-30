"""
LeetCode Problem: Subsets
Category: Backtracking
Link: https://leetcode.com/problems/subsets/
Approach: DFS/backtracking to include or exclude each element

Time Complexity: O(2^n · n)  # generate all subsets and copy
Space Complexity: O(n)      # recursion depth + subset storage
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(index: int):
            # once we've considered all positions, record the subset
            if index == len(nums):
                result.append(subset.copy())
                return

            # include nums[index]
            subset.append(nums[index])
            dfs(index + 1)

            # exclude nums[index]
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return result
