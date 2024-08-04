import collections
from typing import List


###Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = []
        stack.append(root)

        while stack:
            level = []
            size = len(stack)
            for _ in range(size):
                node = stack.pop(0)
                if not node:
                    continue
                level.append(node.val)
                for child in node.children:
                    stack.append(child)
            if level:
                res.append(level)
        return res


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(level)

        return result
