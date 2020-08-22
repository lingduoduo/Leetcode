# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## recursive
        if not root: return []
        
        res = list()
        
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res
        
        ## reverse post-order
        if not root: return []
        
        res = list()
        visited = list()
        visited.append(root)
        
        while visited:
            node = visited.pop()
            res.append(node.val)
            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)
        return res[::-1]
