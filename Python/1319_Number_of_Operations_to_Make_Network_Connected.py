from typing import List
from collections import Counter
import heapq
import re
from collections import deque
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        self.rank[rx] += 1
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)
        for u, v in connections:
            uf.union(u, v)

        roots = set()
        for i in range(n):
            roots.add(uf.find(i))

        return len(roots) - 1

if __name__ == "__main__":
    res = Solution().makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]])
    print(res)
