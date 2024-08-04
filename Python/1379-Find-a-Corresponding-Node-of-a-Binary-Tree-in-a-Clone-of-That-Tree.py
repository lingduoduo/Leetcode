# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        if original == target:
            return cloned
        if original.left:
            res = self.getTargetCopy(original.left, cloned.left, target)
            if res:
                return res
        if original.right:
            res = sself.getTargetCopy(original.right, cloned.right, target)
            if res:
                return res
