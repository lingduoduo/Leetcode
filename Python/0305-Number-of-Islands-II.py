from typing import List


class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        self.root[self.find(x)] = self.root[self.find(y)]


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = DSU(m * n)
        visited = set()
        res, island = [], 0
        for r, c in positions:
            p = r * n + c
            if p not in visited:
                visited.add(p)
                island += 1
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n:
                    np = nr * n + nc
                    if np in visited and uf.find(p) != uf.find(np):
                        uf.union(p, np)
                        island -= 1
            res.append(island)
        return res
