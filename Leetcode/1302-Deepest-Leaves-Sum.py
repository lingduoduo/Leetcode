# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stack = [root]

        while stack:
            res = 0
            for i in range(len(stack)):
                node = stack.pop(0)
                res += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res
        