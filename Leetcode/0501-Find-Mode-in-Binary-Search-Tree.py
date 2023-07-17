# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = []
        self.dfs(root)
        col = collections.Counter(self.res)
        val = col.most_common(1)[0][1]
        return list(filter(lambda k: col[k] == val, col))

    def dfs(self, root):
        if not root:
            return

        self.res.append(root.val)
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)


import collections


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            nonlocal d
            if not root:
                return
            d[root.val] += 1
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        d = collections.defaultdict(int)
        traverse(root)
        mv = max([i for i in d.values()])
        res = []
        for k, v in d.items():
            if v == mv:
                res.append(k)
        return res


class Solution:
    def __init__(self):
        self.maxCount = 0  # 最大频率
        self.count = 0  # 统计频率
        self.pre = None
        self.result = []

    def searchBST(self, cur):
        if cur is None:
            return

        self.searchBST(cur.left)  # 左
        # 中
        if self.pre is None:  # 第一个节点
            self.count = 1
        elif self.pre.val == cur.val:  # 与前一个节点数值相同
            self.count += 1
        else:  # 与前一个节点数值不同
            self.count = 1

        self.pre = cur  # 更新上一个节点

        if self.count == self.maxCount:  # 如果与最大值频率相同，放进result中
            self.result.append(cur.val)

        if self.count > self.maxCount:  # 如果计数大于最大值频率
            self.maxCount = self.count  # 更新最大频率
            self.result = [cur.val]  # 很关键的一步，不要忘记清空result，之前result里的元素都失效了

        self.searchBST(cur.right)  # 右
        return

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count = 0
        self.maxCount = 0
        self.pre = None  # 记录前一个节点
        self.result = []

        self.searchBST(root)
        return self.result
