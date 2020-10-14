# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root: return None

        res = self.dfs(root)
        return res[0]

    def dfs(self, root):
        if not root:
            return root, -1

        left, leftHeight = self.dfs(root.left)
        right, rightHeight = self.dfs(root.right)
        height = max(leftHeight, rightHeight) + 1

        if leftHeight == rightHeight:
            return root, height
        elif leftHeight < rightHeight:
            return right, height
        else:
            return left, height
