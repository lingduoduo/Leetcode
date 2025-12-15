from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n <= 1:
            return 0

        full = (1 << n) - 1
        q = deque()
        dist = [[-1] * (1 << n) for _ in range(n)]

        for i in range(n):
            m = 1 << i
            q.append((i, m))
            dist[i][m] = 0

        while q:
            node, mask = q.popleft()
            d = dist[node][mask]
            if mask == full:
                return d

            for nei in graph[node]:
                nmask = mask | (1 << nei)
                if dist[nei][nmask] == -1:
                    dist[nei][nmask] = d + 1
                    q.append((nei, nmask))

        return -1
