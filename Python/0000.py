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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(i):
                print(i, j, isConnected[i][j])
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return sum(i == v for i, v in enumerate(uf.par))

if __name__ == "__main__":
    res = Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
    print(res)