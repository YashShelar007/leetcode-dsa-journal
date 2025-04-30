"""
LeetCode Problem: Fibonacci Number
Category: Recursion
Link: https://leetcode.com/problems/fibonacci-number/
Approach: Simple recursion

Time Complexity: O(2^n)
Space Complexity: O(n)  # call stack
"""

class Solution:
    def fib(self, n: int) -> int:
        # base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        # recurse on two previous values
        return self.fib(n - 1) + self.fib(n - 2)
