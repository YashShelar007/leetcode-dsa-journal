"""
LeetCode Problem: Longest Substring Without Repeating Characters
Category: Sliding Window
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Approach: Sliding Window with HashMap

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        mp = {}    # maps character -> last seen index
        l = 0      # left boundary of current window
        
        for r, char in enumerate(s):
            # if char seen in current window, move left boundary
            if char in mp and mp[char] >= l:
                l = mp[char] + 1
            # update max length
            result = max(result, r - l + 1)
            # record last seen index of char
            mp[char] = r
        
        return result
