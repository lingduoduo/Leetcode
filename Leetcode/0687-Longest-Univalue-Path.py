###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def univalue(root):
            if root is None:
                return 0

            right = univalue(root.right)
            left = univalue(root.left)
            right_result = 0
            left_result = 0

            if root.right and root.val == root.right.val:
                right_result = right + 1

            if root.left and root.val == root.left.val:
                left_result = left + 1

            self.result = max(self.result, left_result + right_result)
            return max(left_result, right_result)

        univalue(root)
        return self.result

        if not root:
            return 0
        self.res = 0
        self.getPath(root)
        return self.res

    def getPath(self, root):
        if not root:
            return 0
        left = self.getPath(root.left)
        right = self.getPath(root.right)
        pl, pr = 0, 0
        if root.left and root.left.val == root.val:
            pl = 1 + left
        if root.right and root.right.val == root.val:
            pr = 1 + right
        self.res = max(self.res, pl + pr)
        return max(pl, pr)
