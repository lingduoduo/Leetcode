Definition
for a binary tree node.


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
