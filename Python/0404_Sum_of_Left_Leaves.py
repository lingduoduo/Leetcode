###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    self.result = 0

    def trav(root):
        if not root:
            return

        if root.left and not root.left.left and not root.left.right:
            self.result += root.left.val

        trav(root.left)
        trav(root.right)

    trav(root)
    return self.result


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, direction=""):
            if not root:
                return 0
            if not root.left and not root.right:
                if direction == "l":
                    return root.val
            left = 0
            right = 0
            if root.left:
                left = helper(root.left, "l")
            if root.right:
                right = helper(root.right, "r")
            return left + right

        return helper(root, "")


class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        leftValue = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftValue = root.left.val
        return (
            leftValue
            + self.sumOfLeftLeaves(root.left)
            + self.sumOfLeftLeaves(root.right)
        )


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        res = 0
        while stack:
            node = stack.pop(0)
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
