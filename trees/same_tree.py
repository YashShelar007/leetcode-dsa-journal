"""
LeetCode Problem: Same Tree
Category: Trees
Link: https://leetcode.com/problems/same-tree/
Approach: Breadth-First Search (Queue Comparison)

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([p]), deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                n1 = q1.popleft()
                n2 = q2.popleft()
                # both None? continue
                if not n1 and not n2:
                    continue
                # mismatch or one is None
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                # enqueue children for next level
                q1.append(n1.left);  q1.append(n1.right)
                q2.append(n2.left);  q2.append(n2.right)
        return True

"""
LeetCode Problem: Same Tree
Category: Trees
Link: https://leetcode.com/problems/same-tree/
Approach: Depth-First Search (Recursion)

Time Complexity: O(n)
Space Complexity: O(h)


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both empty
        if not p and not q:
            return True
        # both non-empty and values match? recurse
        if p and q and p.val == q.val:
            return (
                self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return False
"""