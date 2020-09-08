# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, path):
            if not node:
                return 

            path = path + [node.val]

            if not node.left and not node.right:
                if self.hasPalindromic(path):
                    self.res += 1

            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, [])
        return self.res

    def hasPalindromic(self, nums):

        d = collections.Counter(nums)

        odds = 0

        for val in d.values():
            if val %2 == 1:
                odds += 1
        return odds <= 1