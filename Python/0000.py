from collections import defaultdict
from typing import List
import math
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0

            res += abs(left - right)

        dfs(root)
        return res
        



        


# if __name__ == "__main__":
#     res = Solution().mergeKLists(lists = [[1,4,5],[1,3,4],[2,6]])
#     print(res)
