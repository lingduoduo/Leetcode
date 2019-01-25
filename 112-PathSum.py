# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
        	return False
        if root.left is None and root.right is None and root.val == sum:
        	return True
        if self.hasPathSum(root.left, sum-root.val):
        	return True
        if self.hasPathSum(root.right, sum-root.val):
        	return True
        return False
