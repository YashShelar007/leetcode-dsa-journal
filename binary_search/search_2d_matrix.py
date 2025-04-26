"""
LeetCode Problem: Search a 2D Matrix
Category: Binary Search
Link: https://leetcode.com/problems/search-a-2d-matrix/
Approach: Binary search to find candidate row, then binary search within that row

Time Complexity: O(log m + log n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        # Locate the row that may contain target
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break

        if top > bot:
            return False

        row = (top + bot) // 2
        l, r = 0, COLS - 1

        # Binary search within the selected row
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False