"""
LeetCode Problem: Implement Queue using Stacks
Category: Stack
Link: https://leetcode.com/problems/implement-queue-using-stacks/
Approach: Reversed-stack push to maintain queue order

Time Complexity:
 - push: O(n)
 - pop/peek/empty: O(1)
Space Complexity: O(n)
"""

class MyQueue:
    def __init__(self):
        # stack1 will always have front of queue at the end
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # move all from stack1 → stack2, push new, then back
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        # pop from stack1 gives the queue front
        return self.stack1.pop()

    def peek(self) -> int:
        # last element of stack1 is the front
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0
