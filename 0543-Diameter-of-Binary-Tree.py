###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None

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
            result = max(result, l + r)
            return max(l, r) + 1
        
        depth(root)
        return result


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.traverse(root)
        return self.res
        
    
    def traverse(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        if root.left: 
            left = self.traverse(root.left)
        else:
            left = 0
    
        if root.right: 
            right = self.traverse(root.right)
        else:
            right = 0
        
        self.res = max(self.res, left + right)
        
        return 1 + max(left, right)