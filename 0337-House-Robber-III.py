# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.d = dict()
        return self.helper(root, False)
    
    def helper(self, root, parentUsed):
        if not root: return 0

        if (root, parentUsed) in self.d:
            return self.d[(root, parentUsed)]

        res = 0

        if parentUsed:
            res = self.helper(root.left, False) + self.helper(root.right, False)
        else:
            res = max(root.val + self.helper(root.left, True) + self.helper(root.right, True), 
                self.helper(root.left, False) + self.helper(root.right, False))
        self.d[(root, parentUsed)] = res
        return res
