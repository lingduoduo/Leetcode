"""
###Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        if len(root.children) == 0: return 1
        
        l = [0] * len(root.children)
        for i in range(len(root.children)):
            l[i] = self.maxDepth(root.children[i])
        return max(l) + 1
