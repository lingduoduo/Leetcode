from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        if not root1:
            return root2
        if not root2:
            return root1

        val = 0
        if root1:
            val += root1.val
        if root2:
            val += root2.val
        root = TreeNode(val)

        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root2:
            return root1
        if not root1:
            return root2
        newT = TreeNode(root1.val + root2.val)
        newT.left = self.mergeTrees(root1.left, root2.left)
        newT.right = self.mergeTrees(root1.right, root2.right)
        return newT