"""
LeetCode Problem: Valid Parentheses
Category: Stack
Link: https://leetcode.com/problems/valid-parentheses/
Approach: Stack matching with map of closing→opening

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # mapping of closing bracket → its corresponding opening
        pairs = {")": "(", "}": "{", "]": "["}

        for ch in s:
            # if it's a closing bracket, check top of stack
            if ch in pairs:
                # if stack empty or top doesn't match expected opening, invalid
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                # opening bracket → push onto stack
                stack.append(ch)
        # valid only if no unmatched openings remain
        return not stack
