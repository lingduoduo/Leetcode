import collections
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        self.res = collections.defaultdict(list)
        self.dfs(root, 0)
        return self.res.values()

    def dfs(self, root, level):
        if not root:
            return

        if level % 2 == 0:
            self.res[level] = self.res[level] + [root.val]
        else:
            self.res[level] = [root.val] + self.res[level]

        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)
        return


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [root]
        cnt = 0
        while stack:
            cnt += 1
            level = []
            for i in range(len(stack)):
                node = stack.pop(0)
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if cnt % 2 == 1:
                res.append(level)
            else:
                res.append(level[::-1])
        return res