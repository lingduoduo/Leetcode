from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dist = collections.defaultdict(list)
        for source, target in edges:
            dist[source].append(target)
            dist[target].append(source)
        count = 0
        visited = set()
        queue = collections.deque()
        for x in range(n):
            if x in visited:
                continue
            queue.append(x)
            while queue:
                source = queue.popleft()
                if source in visited:
                    continue
                visited.add(source)
                for target in dist[source]:
                    queue.append(target)
            count += 1
        return count

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)

        return sum(i == v for i, v in enumerate(uf.par))