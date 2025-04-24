"""
LeetCode Problem: Valid Palindrome
Category: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/
Approach: Two Pointers with Character Filtering

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters from left
            if not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from right
            elif not s[r].isalnum():
                r -= 1
            else:
                # Compare lowercase versions of characters
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        
        return True
