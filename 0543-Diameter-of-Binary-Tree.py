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
        if not root: return 0
        
        self.res = 0
        self.traverse(root)
        return self.res - 1
        
    
    def traverse(self, root):
        if not root:
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        self.res = max(self.res, 1 + left + right)
        
        return 1 + max(left, right)