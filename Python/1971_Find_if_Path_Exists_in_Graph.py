from typing import List
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False

        visited = set()
        return dfs(source, visited)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = collections.defaultdict(list)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])

        stack = [source]
        seen = set([source])
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for new_node in d[node]:
                if new_node not in seen:
                    seen.add(new_node)
                    stack.append(new_node)
        return False


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    
    def find(self, i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        self.par[ri] = rj

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])
        return uf.find(source) == uf.find(destination)


if __name__ == "__main__":
    # res = Solution().validPath(n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2)
    # print(res)

    res = Solution().validPath(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
    print(res)


# 10
# [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
# 7
# 5
