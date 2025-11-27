from typing import List
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        dist = collections.defaultdict(list)
        for n1, n2 in edges:
            dist[n1].append(n2)
            dist[n2].append(n1)

        visited = set()
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for related in dist[node]:
                if related not in visited:
                    visited.add(related)
                    queue.append(related)
        return len(visited) == n


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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = DSU(n)
        for r, c in edges:
            if uf.find(r) != uf.find(c):
                uf.union(r, c)
            else:
                return False
        return True


if __name__ == "__main__":
    res = Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])
    print(res)
