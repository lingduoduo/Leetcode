"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # res = []
        # if not root:
        #     return res
        # res.append(root.val)
        # for child in root.children:
        #     res.extedn(self.preorder(child))
        # return res

        if not root: return []
        stack = []
        stack.append(root)
        res =[]
        while stack:
            node =stack.pop()
            res.append(node.val)
            for child in childen:
                res.append(node.val)
                stack.extend(node.children[::-1])
            return res
