# Definition for a binary tree node.
class TreeNode:
    def __init__(self, root, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.dfs(root.right)


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if left_height == right_height:
            nodes = 2**left_height + self.countNodes(root.right)
        else:
            nodes = 2**right_height + self.countNodes(root.left)
        return nodes

    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftDepth = 0  # 这里初始为0是有目的的，为了下面求指数方便
        rightDepth = 0
        while left:  # 求左子树深度
            left = left.left
            leftDepth += 1
        while right:  # 求右子树深度
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return (2 << leftDepth) - 1  # 注意(2<<1) 相当于2^2，所以leftDepth初始为0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


class Solution:  # 利用完全二叉树特性
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1
        left = root.left
        right = root.right
        while left and right:
            count += 1
            left = left.left
            right = right.right
        if not left and not right:  # 如果同时到底说明是满二叉树，反之则不是
            return 2**count - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution:  # 利用完全二叉树特性
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        left = root.left
        right = root.right
        while left and right:
            count += 1
            left = left.left
            right = right.right
        if not left and not right:  # 如果同时到底说明是满二叉树，反之则不是
            return (2 << count) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
