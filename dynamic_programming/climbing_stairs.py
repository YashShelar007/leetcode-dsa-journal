"""
LeetCode Problem: Climbing Stairs
Category: Dynamic Programming
Link: https://leetcode.com/problems/climbing-stairs/
Approach: Iterative Fibonacci-like DP

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # one = ways to reach current step
        # two = ways to reach previous step
        one, two = 1, 1
        # build up from step 2 to n
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
