###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = 0
        self.result = 0

        def DFS(root, k):
            if root is None:
                return
            DFS(root.left, k)
            self.cnt += 1
            if self.cnt == k:
                self.result = root.val
            DFS(root.right, k)

        DFS(root, k)
        return self.result


# 递归
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if not root:
                return
            res = inorder(root.left)
            if res is not None:
                return res
            self.k -= 1
            if self.k == 0:
                return root.val
            else:
                return inorder(root.right)

        self.k = k
        return inorder(root)


# 非递归
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
