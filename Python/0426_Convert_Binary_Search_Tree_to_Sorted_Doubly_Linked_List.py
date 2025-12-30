"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        head = None
        prev = None
        def inorder(node):
            nonlocal head, prev
            if not node:
                return

            inorder(node.left)
            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node

            prev = node
            inorder(node.right)

        inorder(root)
        head.left = prev
        prev.right = head
        return head


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return
        dummy = Node(0, None, None)

        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right
