import collections
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        
        stack = []
        node = root
        pre = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.right
                
            node = stack.pop()
            pre += node.val
            node.val = pre
            node = node.left
        return root

