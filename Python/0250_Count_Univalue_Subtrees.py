# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self.is_uni(root)
        return self.res

    def is_uni(self, root):
        if not root:
            return True

        if not root.left and not root.right:
            self.res += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtrees and if they have the same value
        # also recursively call is_uni for children
        if root.left is not None:
            is_uni = self.is_uni(root.left) and is_uni and root.left.val == root.val

        if root.right is not None:
            is_uni = self.is_uni(root.right) and is_uni and root.right.val == root.val

        # increment self.res and return whether a univalue tree exists here
        self.res += is_uni

        return is_uni
