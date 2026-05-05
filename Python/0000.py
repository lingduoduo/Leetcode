from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def union(self, x: int, y: int) -> bool:
        """Union x and y. Return False if they are already connected (cycle)."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        self.par[rx] = ry
        return True
    
class UF:
    def __init__(self, n):
        self.par = list(range(n + 1))
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return False
        else:
            self.par[px] = py
            return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n)
        for x, y in edges:
            if not uf.union(x, y):
                return [x, y]



if __name__ == "__main__":
    print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))