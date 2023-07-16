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
            return validate(node.right, node.val, high) and validate(
                node.left, low, node.val
            )

        return validate(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def traverse(root):
            nonlocal maxnum
            if not root:
                return True

            left = traverse(root.left)
            if maxnum < root.val:
                maxnum = root.val
            else:
                return False
            right = traverse(root.right)
            return left and right

        maxnum = float("-inf")
        return traverse(root)


class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None  # 记录前一个节点
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left  # 左
            else:
                cur = stack.pop()  # 中
                if pre is not None and cur.val <= pre.val:
                    return False
                pre = cur  # 保存前一个访问的结点
                cur = cur.right  # 右
        return True
