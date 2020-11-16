# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        self.traverse(root, [])
        return self.res
    
    
    def traverse(self, root, path):
        if not root:
            return 
        

        for i in range(len(path)):
            self.res = max(self.res, abs(path[i] - root.val))
        
        if root.left:
            self.traverse(root.left, path + [root.val])
        
        if root.right:
            self.traverse(root.right, path + [root.val])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        self.traverse(root, root.val, root.val)
        return self.res
    
    
    def traverse(self, root, gmax, gmin):
        if not root:
            return 
        
        self.res = max(self.res, abs(gmax - root.val), abs(gmin - root.val))
        
        if root.left:
            self.traverse(root.left, max(gmax, root.val), min(gmin, root.val))
        
        if root.right:
            self.traverse(root.right, max(gmax, root.val), min(gmin, root.val))