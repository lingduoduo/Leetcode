# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.balance(root)
        return self.result

    def balance(self, root):
        if root is None:
            return 0
        l = self.balance(root.left)
        r = self.balance(root.right)
        self.result += abs(l) + abs(r)
        return l + r + root.val - 1
