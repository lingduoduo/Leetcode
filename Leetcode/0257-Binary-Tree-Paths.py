# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        self.res = []
        self.dfs(root, [])
        s = []
        for path in self.res:
            s.append("->".join(path))
        return s

    def dfs(self, root, path):
        if not root:
            return

        if not root.left and not root.right:
            self.res.append(path + [str(root.val)])

        if root.left:
            self.dfs(root.left, path + [str(root.val)])
        if root.right:
            self.dfs(root.right, path + [str(root.val)])

        # Definition for a binary tree node.


class Solution:
    def traversal(self, cur, path, result):
        path.append(cur.val)  # 中
        if not cur.left and not cur.right:  # 到达叶子节点
            sPath = "->".join(map(str, path))
            result.append(sPath)
            return
        if cur.left:  # 左
            self.traversal(cur.left, path, result)
            path.pop()  # 回溯
        if cur.right:  # 右
            self.traversal(cur.right, path, result)
            path.pop()  # 回溯

    def binaryTreePaths(self, root):
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(root, path):
            if not root.left and not root.right:
                res.append("->".join(map(str, path + [root.val])))
            if root.left:
                traverse(root.left, path + [root.val])
            if root.right:
                traverse(root.right, path + [root.val])

        res = []
        traverse(root, [])
        return res


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 题目中节点数至少为1
        stack, path_st, result = [root], [str(root.val)], []

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子节点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + "->" + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + "->" + str(cur.left.val))

        return result
