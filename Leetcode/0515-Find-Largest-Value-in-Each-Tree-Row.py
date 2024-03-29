# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        vals = [root.val]
        res = []

        while stack:
            res.append(max(vals))
            for i in range(len(stack)):
                node = stack.pop(0)
                vals.pop(0)
                if node.left:
                    stack.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    stack.append(node.right)
                    vals.append(node.right.val)
        return res


import collections


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            max_val = float("-inf")

            for _ in range(level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(max_val)

        return result
