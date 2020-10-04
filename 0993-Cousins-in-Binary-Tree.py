# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xparent, xdepth = self.findParent(root, x, 0)
        yparent, ydepth = self.findParent(root, y, 0)
        if xparent != yparent and xdepth == ydepth:
            return True
        else:
            return False
    
    
    def findParent(self, root, node, depth):
        if not root or (not root.left and not root.right):
            return 

        if root.left.val==node or root.right.val==node:
            return root, depth+1

        if root.left:
            result = self.findParent(root.left, node, depth+1)
        if root.right:
            result = self.findParent(root.right, node, depth+1)
        return result