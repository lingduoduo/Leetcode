###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ####first try
        result = []
        level = 0

        def bfs(root, level):
            if root is None:
                return
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            bfs(root.left, level + 1)
            bfs(root.right, level + 1)

        bfs(root, 0)
        return result


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        visited = []
        visited.append(root)

        while visited:
            size = len(visited)
            par = []
            while size > 0:
                node = visited.pop(0)
                par.append(node.val)
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
                size -= 1
            result.append(par)
        return result


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        stack = [root]

        while stack:
            nodes = []
            for i in range(len(stack)):
                node = stack.pop(0)
                nodes.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(nodes)
        return res
