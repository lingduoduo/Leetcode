# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        self.res = 0
        
        self.traverse(root, float("-inf"))
        
        return self.res
    
    def traverse(self, root, par):
        if not root: return
        
        if root.val >= par:
            self.res += 1
        
        self.traverse(root.left, max(root.val, par))
        self.traverse(root.right, max(root.val, par))
        
    