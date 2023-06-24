# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, root, left, right):
        if not root:
            return True

        if root.val <= left or root.val >= right:
            return False

        return self.valid(root.left, left, root.val) and self.valid(
            root.right, root.val, right
        )


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(res) == len(set(res))

    def inOrder(self, root, res):
        if not root:
            return []
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=float("-inf"), high=float("inf")):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                    validate(node.left, low, node.val))

        return validate(root)
