"""
LeetCode Problem: Binary Search
Category: Binary Search
Link: https://leetcode.com/problems/binary-search/
Approach: Iterative Two-Pointer Search

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # search window [l…r]

        while l <= r:
            mid = l + (r - l) // 2  # middle index
            if nums[mid] < target:
                l = mid + 1          # target is in the right half
            elif nums[mid] > target:
                r = mid - 1          # target is in the left half
            else:
                return mid           # found target
        
        return -1                  # target not in list
