import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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
        print(d_depth, d_height)

        cousins = collections.defaultdict(list)  
        for val, depth in d_depth.items():
            cousins[depth].append((-d_height[val], val))
            cousins[depth].sort()
            if len(cousins[depth]) > 2:
                cousins[depth].pop()
        print(cousins)

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

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(7)
    res = Solution().treeQueries(root, queries = [4])
    print(res)