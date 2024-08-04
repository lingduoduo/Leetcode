# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        res = self.dfs(root)
        return res[0]

    def dfs(self, root):
        if not root:
            return root, -1

        left, leftHeight = self.dfs(root.left)
        right, rightHeight = self.dfs(root.right)
        height = max(leftHeight, rightHeight) + 1

        if leftHeight == rightHeight:
            return root, height
        elif leftHeight < rightHeight:
            return right, height
        else:
            return left, height


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        parent = {}
        queue = collections.deque([root])
        while queue:
            prev = queue.copy()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)

        while len(prev) > 1:
            prev = set(parent[node] for node in prev)

        return prev.pop()
