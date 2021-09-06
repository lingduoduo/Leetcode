###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None

# class Solution(object):
#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None: return 0
#         result = 0
#
#         def depth(root):
#             if root is None:
#                 return 0
#             if root.left is None and root.right is None:
#                 return 1
#             l = depth(root.left)
#             r = depth(root.right)
#             result = max(result, l + r)
#             return max(l, r) + 1
#
#         depth(root)
#         return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth(root)
        return self.res

    def depth(self, root):
        if not root:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)

        self.res = max(self.res, l + r)

        return 1 + max(l, r)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        self.res = max(self.res,  left + right)
        return max(left+1, right+1)
    