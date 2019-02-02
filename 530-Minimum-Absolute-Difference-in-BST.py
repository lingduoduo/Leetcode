# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        s = list()
        self.inorder(root, s)
        result = s[1]-s[0]
        for i in range(2,len(s)):
        	result = min(result, s[i]-s[i-1])
        return result

    def inorder(self, root, ss):
    	if root is None:
    		return
    	if root.left is None and root.right is None:
    		ss.append(root.val)
    		return
    	self.inorder(root.left, ss)
    	ss.append(root.val)
    	self.inorder(root.right, ss)
        