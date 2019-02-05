# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        result = 0

        
        def depth(root):
        	if root is None:
        		return 0
        	if root.left is None and root.right is None:
        		return 1
        	l = depth(root.left)
        	r = depth(root.right)
        	result = max(result, l+r)
        	return max(l, r)+1
        
        depth(root)
        return result

