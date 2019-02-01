
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
	
		def dfs(left, right):
			if left is None and right is None:
				return True
			if left is None:
				return False
			if right is None:
				return False
			flag1 = dfs(left.left, right.left)
			flag2 = dfs(left.right, right.right)
			if left.val == right.val and flag1  and flag2:
				return True

		if root is None:
        	return True
        if root.left is None and root.right is None:
        	return True
        if root.left is None and root.right is not None:
        	return False
        if root.left is not None and root.right is None:
        	return False
        return True if dfs(root.left, root.right) False
        