from typing import List
from collections import defaultdict, deque


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)

        for s, e, v in roads:
            g[s].append((v, e))
            g[e].append((v, s))

        que = deque([1])
        visited = {1}
        res = float("inf")
        while que:
            node = que.popleft()

            for v, nei in g[node]:
                res = min(res, v)

                if nei not in visited:
                    visited.add(nei)
                    que.append(nei)

        return res
