"""
LeetCode Problem: Merge Intervals
Category: Array & Sorting
Link: https://leetcode.com/problems/merge-intervals/
Approach: Sort + Greedy Merge

Time Complexity: O(n log n)  # for initial sort
Space Complexity: O(n)       # output list
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            # If the current interval overlaps the last merged one, extend it
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                # Otherwise, it’s a new disjoint interval
                merged.append([start, end])

        return merged
