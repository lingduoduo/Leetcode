from typing import List
import heapq


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Build adjacency list; cities are 1..n, convert to 0..n-1
        graph = [[] for _ in range(n)]
        for city1, city2, cost in connections:
            u, v = city1 - 1, city2 - 1
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        in_mst = [False] * n
        heap = [(0, 0)]        # (cost, node), start from node 0 (city 1)
        res = 0
        added = 0

        while heap and added < n:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue
            # take this node into MST
            in_mst[u] = True
            res += cost
            added += 1

            # push all edges from u to neighbors
            for v, w in graph[u]:
                if not in_mst[v]:
                    heapq.heappush(heap, (w, v))

        # if not all cities are connected
        if added < n:
            return -1
        return res
