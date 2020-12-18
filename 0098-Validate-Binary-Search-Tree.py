###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None

class Solution(object):
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.valid(root, float("-inf"), float("inf"))
        
    def valid(self, root, left, right):
        if not root:
            return True
        
        if root.val <= left or root.val >= right:
            return False
        
        return self.valid(root.left, left, root.val) and self.valid(root.right, root.val, right)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(res) == len(set(res))
        
    def inOrder(self, root, res):
        if not root: return []
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
