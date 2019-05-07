# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        
        minVal = root.val
        self.secVal = 0x80000000
        
        def traverse(root):
            if root is None:
                return -1
            if self.secVal > root.val and root.val > minVal:
                self.secVal = root.val
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.secVal if !self.secVal = 0x80000000 else -1
