# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
        	return 0
        if root.left is None and root.right is None:
        	return 1
        leftDepth = minDepth(root.left)
        rightDepth = minDepth(root.right)
        if root.left is None:
        	return rightDepth+1
        if root.right is None:
        	retrun leftDepth+1
        return min(leftDepth, rightDepth)+1

