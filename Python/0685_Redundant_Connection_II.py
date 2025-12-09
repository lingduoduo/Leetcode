class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def cycle(v, p):
            u = p[v]
            while u != 0:
                if u == v:
                    return True
                u = p[u]
            return False

        n = len(edges)
        p = [0] * (n + 1)

        ans1 = []
        ans2 = []
        dup_p = False

        for e in edges:
            u, v = e
            if p[v] > 0:
                ans1 = [p[v], v]
                ans2 = [u, v]
                dup_p = True
                e[0] = e[1] = -1
            else:
                p[v] = u

        p = [0] * (n + 1)

        for u, v in edges:
            if u < 0:
                continue
            p[v] = u
            if cycle(v, p):
                return ans1 if dup_p else [u, v]

        return ans2


from typing import List

class UF:
    def __init__(self, n: int):
        # 0..n, but we usually use 1..n for this problem
        self.par = list(range(n + 1))

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])  # path compression
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        """Union x and y. Return False if they are already connected (cycle)."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        self.par[rx] = ry
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        cand1 = None  # first edge to a node with two parents
        cand2 = None  # second edge to a node with two parents

        # 1. Detect a node with two parents
        for i, (u, v) in enumerate(edges):
            if parent[v] == 0:
                parent[v] = u
            else:
                # v already has a parent -> we found two incoming edges to v
                cand1 = [parent[v], v]  # the earlier edge
                cand2 = [u, v]          # the later edge
                # Invalidate the later edge so it's skipped in UF cycle check
                edges[i][1] = 0

        # 2. Union-Find to detect cycle, ignoring the invalidated edge
        uf = UF(n)
        for u, v in edges:
            if v == 0:   # skip invalidated edge (cand2)
                continue
            if not uf.union(u, v):  # found a cycle
                # If there was a node with two parents, the first edge is redundant
                if cand1:
                    return cand1
                # Otherwise the current edge forms the redundant cycle
                return [u, v]

        # 3. If we never saw a cycle, then the second parent edge is redundant
        return cand2

if __name__ == "__main__":
    res = Solution().findRedundantDirectedConnection(edges = [[1,2],[1,3],[2,3]])
    print(res)
