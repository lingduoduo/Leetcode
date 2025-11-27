# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.d = dict()
        return self.helper(root, False)

    def helper(self, root, parentUsed):
        if not root:
            return 0

        if (root, parentUsed) in self.d:
            return self.d[(root, parentUsed)]

        res = 0

        if parentUsed:
            res = self.helper(root.left, False) + self.helper(root.right, False)
        else:
            res = max(
                root.val + self.helper(root.left, True) + self.helper(root.right, True),
                self.helper(root.left, False) + self.helper(root.right, False),
            )
        self.d[(root, parentUsed)] = res
        return res


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)

            red[root] = root.val + black[root.left] + black[root.right]
            black[root] = max(red[root.left], black[root.left]) + max(
                red[root.right], black[root.right]
            )

        red, black = defaultdict(int), defaultdict(int)
        dfs(root)
        return max(red[root], black[root])


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dp数组（dp table）以及下标的含义：
        # 1. 下标为 0 记录 **不偷该节点** 所得到的的最大金钱
        # 2. 下标为 1 记录 **偷该节点** 所得到的的最大金钱
        def traversal(node):
            # 递归终止条件，就是遇到了空节点，那肯定是不偷的
            if not node:
                return (0, 0)

            left = traversal(node.left)
            right = traversal(node.right)

            # 不偷当前节点, 偷子节点
            val_0 = max(left) + max(right)

            # 偷当前节点, 不偷子节点
            val_1 = node.val + left[0] + right[0]

            return (val_0, val_1)

        dp = traversal(root)
        return max(dp)

    # 要用后序遍历, 因为要通过递归函数的返回值来做下一步计算
