# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def leftmost(node):
            if not node: return []
            if node.left is None and node.right is None:
                return []
            if node.left:
                return [node.val] + leftmost(node.left)
            else:
                return [node.val] + leftmost(node.right)
        def leaves(node):
            if not node: return []
            if node.left is None and node.right is None:
                return [node.val]
            return leaves(node.left) + leaves(node.right)

        def rightmost(node):
            if not node: return []
            if node.left is None and node.right is None:
                return []
            if node.right:
                return rightmost(node.right) + [node.val]
            else:
                return rightmost(node.left) + [node.val]

        return [root.val] + leftmost(root.left) + leaves(root.left) + leaves(root.right) + rightmost(root.right)





