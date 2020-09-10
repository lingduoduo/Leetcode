# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []

        return self.dfs(1, n)

    def dfs(self, left, right):
        if left>right:
            return [None]
        res = []

        for i in range(left, right+1):
            left_nodes = self.dfs(left, i-1)
            right_nodes = self.dfs(i+1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res
        