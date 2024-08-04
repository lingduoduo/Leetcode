from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth(root)
        return self.res

    def depth(self, root):
        if not root:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)

        self.res = max(self.res, l + r)

        return 1 + max(l, r)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def depth(root):
            if not root:
                return 0
            nonlocal res
            l = depth(root.left)
            r = depth(root.right)
            res = max(res, l + r)
            return 1 + max(l, r)

        depth(root)
        return res
