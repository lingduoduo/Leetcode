from typing import List
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        seen.add(0)
        que = collections.deque([0])
        while que:
            node = que.popleft()
            for nei in graph[node]:
                if nei in seen:
                    return False
                que.push(nei)
                seen.add(nei)
        return len(seen) == n


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
    res = Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])
    print(res)
