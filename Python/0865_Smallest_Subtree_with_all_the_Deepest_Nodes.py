from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left

        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return (None, 0)
            l = dfs(root.left)
            r = dfs(root.right)
            depth = max(l[1], r[1]) + 1
            if l[1] < r[1]:
                return (r[0], depth)
            elif r[1] < l[1]:
                return (l[0], depth)
            else:
                return (root, depth)

        return dfs(root)[0]


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return None
        parent = {root: None}
        q = deque([root])

        while q:
            deepest = list(q)
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)

        cur = set(deepest)
        while len(cur) > 1:
            cur = {parent[node] for node in cur}
            
        return next(iter(cur))