# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        d = collections.defaultdict(list)

        def bfs(root):
            stack = [root]
            level = 0

            while stack:
                for i in range(len(stack)):
                    node = stack.pop(0)
                    d[level].append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                level += 1
            return level

        l = bfs(root)

        return d[l - 1][0]


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_depth = float("-inf")
        self.result = None
        self.traversal(root, 0)
        return self.result

    def traversal(self, node, depth):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return

        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_depth = float("-inf")
        self.result = None
        self.traversal(root, 0)
        return self.result

    def traversal(self, node, depth):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return

        if node.left:
            self.traversal(node.left, depth + 1)
        if node.right:
            self.traversal(node.right, depth + 1)


from collections import deque


class Solution:
    def findBottomLeftValue(self, root):
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
