from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = []
        self.search(root, sum, [])
        return self.res

    def search(self, root, sum, path):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == sum:
                self.res.append(path + [root.val])
        newsum = sum - root.val
        self.search(root.left, newsum, path + [root.val])
        self.search(root.right, newsum, path + [root.val])


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        q = [(root, root.val, [root.val])]
        res = []
        while q:
            cur, s, path = q.pop()
            if not cur.left and not cur.right and s == targetSum:
                res.append(path)
            if cur.left:
                q.append((cur.left, s + cur.left.val, path + [cur.left.val]))
            if cur.right:
                q.append((cur.right, s + cur.right.val, path + [cur.right.val]))
        return res


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        self.traversal(root, targetSum, [], result)
        return result

    def traversal(self, node, count, path, result):
        if not node:
            return
        path.append(node.val)
        count -= node.val
        if not node.left and not node.right and count == 0:
            result.append(list(path))
        self.traversal(node.left, count, path, result)
        self.traversal(node.right, count, path, result)
        path.pop()


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == targetSum:
                res.append(path)
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        return res
