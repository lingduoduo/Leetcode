# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(root):
            if not root or self.cur == len(voyage):
                return
            if voyage[self.cur] != root.val:
                self.res = [-1]
                return
            self.cur += 1
            if root.left and root.left.val != voyage[self.cur]:
                self.res.append(root.val)
                dfs(root.right)
                dfs(root.left)
            else:
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)

        self.cur = 0
        self.res = []
        dfs(root)
        if self.res and self.res[0] == -1:
            return [-1]
        return self.res
