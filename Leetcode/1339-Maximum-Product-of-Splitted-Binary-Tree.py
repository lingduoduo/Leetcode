# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        s = 0
        stack = [root]
        while stack:
            node = stack.pop()
            s += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        self.s = s
        self.res = 0
        self.dfs(root)
        return self.res % (10 ** 9 + 7)

    def dfs(self, root):
        if not root:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        self.res = max(self.res, left * (self.s - left), right * (self.s - right))
        return left + right + root.val