# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = float("inf")

        def trav(root):
            if not root:
                return
            nonlocal res

            if abs(target - root.val) < abs(target - res):
                res = root.val
            if root.left: trav(root.left)
            if root.right: trav(root.right)

        trav(root)
        return res


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inorder(root: TreeNode):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return min(inorder(root), key = lambda x: abs(target - x))
