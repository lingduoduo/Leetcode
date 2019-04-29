# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        if root1.val != root2.val:
            return False

        flag1 = self.flipEquiv(root1.left, root2.right)
        flag2 = self.flipEquiv(root1.right, root2.left)

        flag3 = self.flipEquiv(root1.left, root2.left)
        flag4 = self.flipEquiv(root1.right, root2.right)

        if ((flag1 and flag2) or (flag3 and flag4)):
            return True
        else:
            return False
