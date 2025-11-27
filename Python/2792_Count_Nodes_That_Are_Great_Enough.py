# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def traverse(node):
            nonlocal res
            if not node:
                return []

            arr = sorted(traverse(node.left) + traverse(node.right))[:k]
            if len(arr) >= k and arr[-1] < node.val:
                res += 1
            else:
                arr.append(node.val)
            return arr

        traverse(root)
        return res
