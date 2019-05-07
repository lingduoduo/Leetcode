# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(root, min, max):
            if not root:
                return True
            if root.val >= max:
                return False
            if root.val <= min:
                return False
            return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)
        
        return dfs(root, float('-inf'), float('inf'))
