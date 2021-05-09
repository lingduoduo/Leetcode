# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.d = collections.defaultdict(list)
        self.dfs(root, 0, 0)

        res = []
        for k in sorted(self.d.keys()):
            level = [val for y, val in sorted(self.d[k], key = lambda x:(-x[0], x[1]))]
            res.append(level)
        return res

    def dfs(self, root, x, y):
        if not root:
            return
        
        self.d[x].append((y, root.val))
            
        if root.left:
            self.dfs(root.left, x-1, y-1)
        if root.right:
            self.dfs(root.right, x+1, y-1)


