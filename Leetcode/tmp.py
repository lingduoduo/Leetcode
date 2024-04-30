from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node):
            return 0 if not node else 1 + max(height(node.left), height(node.right))

        def fill(node, h, l, r):
            if not node:
                return
            mid = (l + r) // 2
            res[h][mid] = str(node.val)
            fill(node.left, h + 1, l, mid - 1)
            fill(node.right, h + 1, mid + 1, r)

        h = height(root)
        w = 2 ** h - 1
        res = [[''] * w for _ in range(h)]
        fill(root, 0, 0, w - 1)
        return res