import collections
from typing import List


# Union Find Method
class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1

        return True


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


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [-1] * (len(edges) + 1)  # -1 is giving me 98% time

        def find(x):
            while self.parent[x] > 0:
                x = self.parent[x]
            return x

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False
            else:
                self.parent[root_x] = root_y
                return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]


class Solution:
    def __init__(self):
        """
        初始化
        """
        self.n = 1005
        self.father = [i for i in range(self.n)]

    def find(self, u):
        """
        并查集里寻根的过程
        """
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    def join(self, u, v):
        """
        将v->u 这条边加入并查集
        """
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u
        pass

    def same(self, u, v):
        """
        判断 u 和 v是否找到同一个根，本题用不上
        """
        u = self.find(u)
        v = self.find(v)
        return u == v

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for i in range(len(edges)):
            if self.same(edges[i][0], edges[i][1]):
                return edges[i]
            else:
                self.join(edges[i][0], edges[i][1])
        return []


if __name__ == "__main__":
    edges = [[1, 2], [1, 3], [2, 3]]
    result = Solution().findRedundantConnection(edges)
    print(result)
