# Definition for a binary tree node.
from typing import List, Optional
import collections
import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        next_level = deque(
            [
                root,
            ]
        )
        rightside = []

        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)

        return rightside


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        right_view = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    right_view.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view
