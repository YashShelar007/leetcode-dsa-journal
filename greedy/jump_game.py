"""
LeetCode Problem: Jump Game
Category: Greedy
Link: https://leetcode.com/problems/jump-game/
Approach: Backward Greedy (track reachable goal)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # position we need to reach

        # Work backwards: can we move from i to at least the current goal?
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i  # update goal to this index

        # If we can "reach" index 0, we can reach the end
        return goal == 0
