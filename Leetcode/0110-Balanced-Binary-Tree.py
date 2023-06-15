###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


# class Solution(object):
###    def getHeight(self, root):
#
###        if root is None:
###            return 0
###    if root.left is None and root.right is None:
###        return 1
###    left = self.getHeight(root.left)
###    right = self.getHeight(root.right)
###    return max(left, right) + 1
#
#
# def isBalanced(self, root):
#     """
#     :type root: TreeNode
#     :rtype: bool
#     """
###    if root is None:
###        return True
###    leftHeight = getHeight(root.left)
###    rightHeight = getHeight(root.right)
###    diff = abs(leftHeight - rightHeight)
###    if diff <= 1 and isBalanced(root.left) and isBalanced(root.right):
###        return True
###    return False

#     if not root:
#         return True
#     if not root.left and not root.right:
#         return True
#     left = self.get_height(root.left)
#     right = self.get_height(root.right)
#     if abs(left-right)<= and isBalanced(root.left) and isinstance((root.right)):
#         return True
#     else:
#         return False
#
#
# def get_height(self, root):
#     if not root:
#         return 0
#     if not root.left and not root.right:
#         return 1
#     if not root.left:
#         return 1+self.get_height(root.right)
#     if not root.right:
#         return 1+self.get_height(root.left)
#
#     return 1+max(self.get_height(root.left), self.get_height(root.right))

from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root):
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if abs(l - r) > 1:
            self.res = False
        return 1 + max(l, r)
