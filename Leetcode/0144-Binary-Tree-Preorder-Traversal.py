###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        visited = []
        res = []
        visited.append(root)
        while visited:
            for i in range(len(visited)):
                node = visited.pop()
                res.append(node.val)
                if node.right:
                    visited.append(node.right)
                if node.left:
                    visited.append(node.left)
        return res
