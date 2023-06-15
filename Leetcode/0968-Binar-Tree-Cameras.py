# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node, par):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered) or (
                    node.left not in covered or node.right not in covered
                ):
                    self.res += 1
                    covered.update({node, par, node.left, node.right})

        self.res = 0
        covered = {None}
        dfs(root, None)
        return self.res
