# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        self.res = []

        self.dfs(root, [])
        
        s = []
        for path in self.res:
            s.append('->'.join(path))
        return s

    def dfs(self, root, path):
        if not root:
            return 

        if not root.left and not root.right:
            self.res.append(path+[str(root.val)])

        if root.left:
            self.dfs(root.left, path+[str(root.val)])
        if root.right:
            self.dfs(root.right, path+[str(root.val)])