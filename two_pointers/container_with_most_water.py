"""
LeetCode Problem: Container With Most Water
Category: Two Pointers
Link: https://leetcode.com/problems/container-with-most-water/
Approach: Two Pointers (Greedy shrinking)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            # Calculate current area
            area = min(height[l], height[r]) * (r - l)
            # Update max area if current is greater
            maxArea = max(maxArea, area)

            # Move the pointer with the smaller height
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea
