"""
###Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]
        next = []
        
        while cur:
            tmp = []
            for n in cur:
                tmp.append(n.val)
                for c in n.children:
                    next.append(c)
            res.append(tmp)
            cur = next
            next = []
        return res
