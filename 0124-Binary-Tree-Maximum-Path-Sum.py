# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        # base case
        if not self.root:
            return 0
        
        # calculate max path sum
        left = 0 if not self.root.left else max(0, self.dfs(self.root.left))
        right = 0 if not self.root.right else max(0, self.dfs(self.root.right))
        
        curr = root.val + left + right
        self.res = max(self.res, curr)
        
        return root.val + max(left, right)
