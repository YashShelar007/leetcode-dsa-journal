"""
LeetCode Problem: Letter Combinations of a Phone Number
Category: Backtracking
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Approach: DFS/backtracking over digit-to-letters mapping

Time Complexity: O(4^n · n)  # worst-case branching factor 4
Space Complexity: O(n)      # recursion depth + current string
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        # mapping digits to their letters
        digitToChar = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "qprs", "8": "tuv", "9": "wxyz",
        }

        def backtrack(index: int, path: str):
            # once we've built a full-length string, record it
            if len(path) == len(digits):
                result.append(path)
                return
            # explore each letter mapped to current digit
            for ch in digitToChar[digits[index]]:
                backtrack(index + 1, path + ch)

        # kick off recursion only if digits is non-empty
        if digits:
            backtrack(0, "")
        return result
