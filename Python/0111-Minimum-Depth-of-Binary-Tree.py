###Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        self.res = []

        self.dfs(root, 1)

        return min(self.res)

    def dfs(self, root, level):
        if not root:
            return level

        if not root.left and not root.right:
            return self.res.append(level)

        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = float("inf")

        def helper(root, depth):
            nonlocal res
            if not root:
                return depth
            if not root.left and not root.right:
                res = min(res, depth + 1)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)

        helper(root, 0)
        return res


if __name__ == "__main__":
    ###root = TreeNode(3)
    ###root.left = TreeNode(9)
    ###root.right = TreeNode(20)
    ###root.right.left = TreeNode(15)
    ###root.right.right = TreeNode(7)

    root = TreeNode(1)
    root.left = TreeNode(2)
    result = Solution().minDepth(root)
    print(result)
