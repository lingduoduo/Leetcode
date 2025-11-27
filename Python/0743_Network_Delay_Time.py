import collections
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        K -= 1
        nodes = collections.defaultdict(list)

        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))

        dist = [float("inf")] * N
        dist[K] = 0
        done = set()

        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)

        return -1 if float("inf") in dist else max(dist)


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = collections.defaultdict(list)
        for u, v, w in times:
            d[u].append([w, v])

        stack = [(0, k)]
        seen = set()
        while stack:
            time, node = heapq.heappop(stack)
            seen.add(node)

            if len(seen) == n:
                return time

            for next_time, next_node in d[node]:
                if next_node not in seen:
                    heapq.heappush(stack, [time + next_time, next_node])
        return -1
