"""
LeetCode Problem: Invert Binary Tree
Category: Trees
Link: https://leetcode.com/problems/invert-binary-tree/
Approach: Breadth-First Search (Level Order)

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        while q:
            node = q.popleft()
            # swap children
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root

"""
LeetCode Problem: Invert Binary Tree
Category: Trees
Link: https://leetcode.com/problems/invert-binary-tree/
Approach: Depth-First Search (Recursion)

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap children
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
"""