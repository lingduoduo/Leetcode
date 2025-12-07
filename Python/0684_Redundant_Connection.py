import collections
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    
    def find(self, i):
        if i != self.par[i]:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
        
    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        self.par[ri] = rj

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for x, y in edges:
            nodes.add(x)
            nodes.add(y)

        d = {}
        for i, v in enumerate(sorted(nodes)):
            d[v] = i

        uf = UnionFind(len(nodes))

        for x, y in edges:
            a, b = d[x], d[y]
            if uf.find(a) == uf.find(b):
                return [x, y]
            uf.union(a, b)

if __name__ == "__main__":
    edges = [[1, 2], [1, 3], [2, 3]]
    result = Solution().findRedundantConnection(edges)
    print(result)
