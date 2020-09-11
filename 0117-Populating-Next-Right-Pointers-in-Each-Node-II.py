"""
###Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
            
        stack = []
        stack.append(root)

        while stack:
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if i<n-1:
                    node.next = stack[0]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root
