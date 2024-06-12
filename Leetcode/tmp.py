from  collections import Counter
from typing import List, Optional
import math
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root, None)

        nodes = []
        def travese(r, d):
            if not r:
                return
            if d == 0:
                nodes.append(r)
                return
            travese(r.left, d - 1)
            travese(r.right, d - 1)

        travese(root, d - 2)
        for node in nodes:
            node.left = TreeNode(v, node.left, None)
            node.right = TreeNode(v, None, node.right)
        return root

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(root, val, depth):
            if root==None: return
            if depth>2:
                dfs(root.left, val, depth-1)
                dfs(root.right, val, depth-1)
            else:
                root.left=TreeNode(val, root.left, None)
                root.right=TreeNode(val, None, root.right)
        if depth == 1:
            return TreeNode(val, root, None)
        dfs(root, val, depth)
        return root

if __name__ == "__main__":
    res = Solution().evenOddBit(n = 5)
    print(res)

