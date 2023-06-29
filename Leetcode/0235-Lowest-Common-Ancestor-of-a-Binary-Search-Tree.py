class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        pointer = root

        while pointer:
            if p.val > pointer.val and q.val > pointer.val:
                pointer = pointer.right
            elif p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
            else:
                return pointer
