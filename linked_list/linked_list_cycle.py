"""
LeetCode Problem: Linked List Cycle
Category: Linked List
Link: https://leetcode.com/problems/linked-list-cycle/
Approach: Two Pointers (Floyd’s Tortoise and Hare)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head      # moves one step at a time
        fast = head      # moves two steps at a time

        # Advance pointers; if they ever meet, there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False  # fast reached the end → no cycle
