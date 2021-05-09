"""
###Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ###if not root:
        ###    return []

        ###res = []
        ###for child in children:
        ###    res.extend(self.postorder(child))
        ###res.append(root.val)
        ###return res

        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]

