"""
LeetCode Problem: Two Sum
Category: Arrays & Hashing
Link: https://leetcode.com/problems/two-sum/
Approach: HashMap (One-pass)

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementDict = {}  # Stores value: index pairs
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complementDict:
                return [complementDict[complement], i]
            complementDict[num] = i  # Store the index of the current number
