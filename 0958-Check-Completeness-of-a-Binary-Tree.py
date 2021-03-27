# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [root]
        hasNone = False

        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if not node:
                    hasNone = True
                    continue
                if hasNone:
                    return False
                
                stack.append(node.left)
                stack.append(node.right)
        return True 





