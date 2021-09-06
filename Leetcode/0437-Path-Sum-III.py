###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


# class Solution(object):
#     def pathSum(self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: int
#         """
        if not root:
            return 0

        res = self.dfs(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res


    def dfs(self, root, targetSum):
        if not root: return 0

        partial = 0
        if root.val == targetSum:
            partial += 1

        partial += self.dfs(root.left, targetSum - root.val)
        partial += self.dfs(root.right, targetSum - root.val)

        return partial

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.parts(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def parts(self, root, target):
        if not root:
            return 0

        res = 0
        if root.val == target:
            res += 1

        res += self.parts(root.left, target - root.val)
        res += self.parts(root.right, target - root.val)

        return res


