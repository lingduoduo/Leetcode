# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = []
        self.dfs(root)
        col = collections.Counter(self.res)
        val = col.most_common(1)[0][1]
        return list(filter(lambda k: col[k] == val, col))

    def dfs(self, root):
        if not root:
            return

        self.res.append(root.val)
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
