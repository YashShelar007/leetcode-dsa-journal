"""
LeetCode Problem: Group Anagrams
Category: Arrays & Hashing
Link: https://leetcode.com/problems/group-anagrams/
Approach: Character Count Hashing

Time Complexity: O(n * k), where n is the number of strings and k is the maximum length of a string
Space Complexity: O(n), for storing grouped anagrams
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for anagram in strs:
            count = [0] * 26  # Count of each character a-z
            for letter in anagram:
                count[ord(letter) - ord('a')] += 1
            # Use character count tuple as the key
            anagramDict[tuple(count)].append(anagram)

        return list(anagramDict.values())
