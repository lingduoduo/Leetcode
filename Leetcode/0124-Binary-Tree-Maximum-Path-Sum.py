###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        self.res = float("-inf")
        self.dfs(root)
        return self.res

    def dfs(self, root):
        ## base case
        if not root:
            return 0

        ## calculate max path sum
        left = 0 if not root.left else max(0, self.dfs(root.left))
        right = 0 if not root.right else max(0, self.dfs(root.right))

        curr = root.val + left + right
        self.res = max(self.res, curr)

        return root.val + max(left, right)


class Solution(object):
    def maxPathSum(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        self.res = float("-inf")

        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0

        left = max(0, self.traverse(root.left))
        right = max(0, self.traverse(root.right))

        self.res = max(self.res, left + right + root.val)
        return root.val + max(left, right)
