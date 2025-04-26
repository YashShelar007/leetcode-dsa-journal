"""
LeetCode Problem: Search a 2D Matrix II
Category: Matrix / Binary Search
Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Approach: Start from top-right and eliminate a row or column each step

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1   # start at top-right corner

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1     # eliminate this column
            elif matrix[r][c] < target:
                r += 1     # eliminate this row
            else:
                return True
        return False