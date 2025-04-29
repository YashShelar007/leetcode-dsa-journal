"""
LeetCode Problem: Maximum Depth of Binary Tree
Category: Trees
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 0
        # process level by level
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth


"""
LeetCode Problem: Maximum Depth of Binary Tree
Category: Trees
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Approach: Depth-First Search (Recursion)

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height (stack)


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # recurse on left/right subtrees and take the larger
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
"""