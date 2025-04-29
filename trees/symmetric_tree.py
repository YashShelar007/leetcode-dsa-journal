"""
LeetCode Problem: Symmetric Tree
Category: Trees
Link: https://leetcode.com/problems/symmetric-tree/
Approach: Depth-First Search (Recursion)

Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            # compare outer and inner pairs
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
