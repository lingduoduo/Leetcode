"""
###Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        # if not root:
        #     return []
        # res = []
        # cur = [root]
        # next = []

        # while cur:
        #     tmp = []
        #     for n in cur:
        #         tmp.append(n.val)
        #         for c in n.children:
        #             next.append(c)
        #     res.append(tmp)
        #     cur = next
        #     next = []
        # return res

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
