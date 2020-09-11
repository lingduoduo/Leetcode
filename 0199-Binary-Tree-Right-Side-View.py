# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root, 0)

        nums = []
        for level in range(len(self.res)):
            nums.append(self.res[level][-1])
        return nums



    def dfs(root, level):
        if not root:
            return

        if len(self.res)==level:
            res.append([])

        res[level].append(root.val)
        if root.left:
            self.dfs(root.left, level+1)
        if root.right:
            self.dfs(root.right, level+1)

