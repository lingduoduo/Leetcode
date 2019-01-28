# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
        	return ""
        s = str(x)
        if t.left is None and t.right is None:
        	return s
        l = tree2str(root.left)
        r = tree2str(root.right)
        if t.right is None:
        	return s+"("+l+")"
        return s+"("+l+")"+"("+r+")"


