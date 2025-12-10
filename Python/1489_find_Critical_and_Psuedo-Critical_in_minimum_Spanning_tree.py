from typing import List

class UnionFind:
    def __init__(self, n: int) -> None:
        # parent[i] = parent of node i
        self.parent = list(range(n))
        # rank[i] = approximate height of tree rooted at i
        self.rank = [0] * n
        # how many connected components remain
        self.set_count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        # attach lower-rank tree under higher-rank tree
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.set_count -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Copy edges and attach original index: [u, v, w] -> [u, v, w, idx]
        edges_with_index = [edge[:] for edge in edges]
        for idx, edge in enumerate(edges_with_index):
            edge.append(idx)

        # Sort by weight
        edges_with_index.sort(key=lambda e: e[2])

        # 1. Compute baseline MST weight (std_weight)
        uf = UnionFind(n)
        std_weight = 0
        for u, v, w, _ in edges_with_index:
            if uf.union(u, v):
                std_weight += w

        critical = []
        pseudo_critical = []

        # 2. For each edge, check critical & pseudo-critical
        for u, v, w, idx in edges_with_index:
            # --- Check if this edge is critical: ignore it and build MST ---
            uf_ignore = UnionFind(n)
            ignore_weight = 0
            for a, b, w2, idx2 in edges_with_index:
                if idx2 == idx:  # skip this edge
                    continue
                if uf_ignore.union(a, b):
                    ignore_weight += w2

            # If graph is disconnected or weight becomes larger -> critical
            if uf_ignore.set_count > 1 or ignore_weight > std_weight:
                critical.append(idx)
                continue

            # --- Check if this edge is pseudo-critical: force it first ---
            uf_force = UnionFind(n)
            force_weight = w
            uf_force.union(u, v)  # force using this edge

            for a, b, w2, idx2 in edges_with_index:
                if idx2 == idx:  # already added
                    continue
                if uf_force.union(a, b):
                    force_weight += w2

            # If forcing it still gives MST weight -> pseudo-critical
            if force_weight == std_weight:
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]
