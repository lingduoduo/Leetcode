# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = []
        self.traverse(root)
        dif = float("inf")
        for i in range(1, len(self.res)):
            dif = min(dif, self.res[i] - self.res[i - 1])
        return dif

    def traverse(self, root):
        if not root:
            return 0

        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
