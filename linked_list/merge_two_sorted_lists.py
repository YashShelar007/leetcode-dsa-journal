"""
LeetCode Problem: Merge Two Sorted Lists
Category: Linked List
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Approach: Iterative merge with dummy head

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)  # start of the merged list
        tail = dummy         # points to last node in merged list

        # Merge until one list is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next

        # Append the remaining nodes
        tail.next = list1 if list1 else list2
        return dummy.next
