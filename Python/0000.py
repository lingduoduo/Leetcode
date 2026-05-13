from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cand, path):
            if len(path) >= 2:
                res.append(path)
            
            used = set()
            for i in range(len(cand)):
                if cand[i] in used:
                    continue
                if path and cand[i] < path[-1]:
                    continue
                used.add(cand[i])
                dfs(cand[i+1:], path + [cand[i]])
        dfs(nums, [])
        return res

if __name__ == "__main__":
    print(Solution().findSubsequences())