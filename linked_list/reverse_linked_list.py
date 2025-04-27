"""
LeetCode Problem: Reverse Linked List
Category: Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Approach: Iterative in-place reversal

Time Complexity: O(n)
Space Complexity: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None   # will become new tail
        curr = head   # iterator through the list

        while curr:
            nxt = curr.next  # save next node
            curr.next = prev # reverse the pointer
            prev = curr      # move prev forward
            curr = nxt       # move curr forward

        return prev
