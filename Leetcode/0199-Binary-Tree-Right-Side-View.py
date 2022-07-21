# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root, 0)

        nums = []
        for level in range(len(self.res)):
            nums.append(self.res[level][-1])
        return nums

    def dfs(root, level):
        if not root:
            return

        if len(self.res) == level:
            res.append([])

        res[level].append(root.val)
        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.res = collections.defaultdict(list)
        self.dfs(root, 0)

        nums = []
        for k, v in self.res.items():
            nums.append(v[-1])
        return nums

    def dfs(self, root, level):
        if not root:
            return

        self.res[level].append(root.val)
        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, max_depth = {}, 0
        stack = [(root, 0)]
        while stack:
            cur, depth = stack.pop()
            max_depth = max(max_depth, depth)
            res.setdefault(depth, cur.val)
            if cur.left:
                stack.append((cur.left, depth + 1))
            if cur.right:
                stack.append((cur.right, depth + 1))
        return [res[depth] for depth in range(max_depth + 1)]
