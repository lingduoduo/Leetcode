# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        S = [root.val]
        stack = [root.left, root.right]
        
        while stack:
            node = stack.pop()
            if node:
                if k-node.val in S:
                    return True
                S.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return False