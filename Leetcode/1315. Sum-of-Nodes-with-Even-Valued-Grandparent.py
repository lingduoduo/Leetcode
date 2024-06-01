from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helper(root: TreeNode, parent: int, gParent: int) -> int:
            if not root:
                return 0

            # Sum values from left and right children, updating parent and grandparent
            leftSum = helper(root.left, root.val, parent)
            rightSum = helper(root.right, root.val, parent)
            rootVal = root.val if gParent % 2 == 0 else 0

            return leftSum + rightSum + rootVal

        return helper(root, -1, -1)  # Initial call with invalid parent and grandparent values