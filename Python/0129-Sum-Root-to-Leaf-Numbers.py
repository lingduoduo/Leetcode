###Definition for a binary tree node.
###class TreeNode:
###    def __init__(self, val=0, left=None, right=None):
###        self.val = val
###        self.left = left
###        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0

        self.dfs(root, 0)

        return self.res


def dfs(self, root, partial):
    if not root:
        return

    if not root.left and not root.right:
        self.res += partial * 10 + root.val

    self.dfs(root.left, partial * 10 + root.val)
    self.dfs(root.right, partial * 10 + root.val)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def trav(root, val):
            if not root:
                return 0

            nonlocal res

            if not root.left and not root.right:
                res += val * 10 + root.val

            trav(root.left, val * 10 + root.val)
            trav(root.right, val * 10 + root.val)

        trav(root, 0)
        return res
