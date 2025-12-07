from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        self.par[rx] = ry

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        uf = UnionFind(n)
        for x, y in edges:
            if uf.find(x) == uf.find(y):
                return False
            uf.union(x, y)
        
        return True

if __name__ == "__main__":
    res = Solution().accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
    print(res)