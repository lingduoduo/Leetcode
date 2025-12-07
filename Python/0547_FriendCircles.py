from typing import List
import collections


class Solution(object):
    def findCircleNum(self, M):
        cnt, n = 0, len(M)
        self.vset = set()
        for x in range(n):
            if x not in self.vset:
                cnt += 1
                self.dfs(M, x)
        return cnt

    def dfs(self, M, n):
        for x in range(len(M)):
            if M[n][x] and x not in self.vset:
                self.vset.add(x)
                self.dfs(M, x)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        graph = collections.defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1):
                if isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)

        seen = set()

        def dfs(u):
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    dfs(v)

        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                seen.add(i)
                dfs(i)
        return res


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
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return sum(i == v for i, v in enumerate(uf.par))
