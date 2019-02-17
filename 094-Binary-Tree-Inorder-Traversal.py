# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Recursive solution
        if root is None: return []
        result = list()

        def dfs(root):
            if root is None: 
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return result
        
        # iterative solution
        stack = []
        result = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                return result
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right