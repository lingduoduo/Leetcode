from typing import Optional


###Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root


import collections


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for i in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        stack = [root]
        while stack:
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                if i == size - 1:
                    node.next = None
                else:
                    node.next = stack[0]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root
