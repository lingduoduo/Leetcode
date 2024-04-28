import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        d_depth, d_height = collections.defaultdict(int), collections.defaultdict(int)

        def dfs(node, depth):
            if not node:
                return -1
            d_depth[node.val] = depth
            d_height[node.val] = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            return d_height[node.val]
        dfs(root, 0)

        cousins = collections.defaultdict(list)  
        for val, depth in d_depth.items():
            cousins[depth].append((-d_height[val], val))
            cousins[depth].sort()
            if len(cousins[depth]) > 2:
                cousins[depth].pop()

        res = []
        for q in queries:
            depth = d_depth[q]
            if len(cousins[depth]) == 1:  
                res.append(depth - 1)
            elif cousins[depth][0][1] == q:  
                res.append(-cousins[depth][1][0] + depth)
            else:  
                res.append(-cousins[depth][0][0] + depth)
        return res
