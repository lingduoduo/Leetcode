# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
	def getHeight(self, root):
        if root is None:
    		return 0
    	if root.left is None and root.right is None:
    		return 1
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)
        diff = abs(leftHeight-rightHeight)
        if diff<=1 and isBalanced(root.left) and isBalanced(root.right):
            return True
        return False
