class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        K -= 1

        nodes = collections.defaultdict(list)

        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))

        dist = [float('inf')] * N
        dist[K] = 0

        visited = set()
        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in visited)[1]

            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
                    
            visited.add(smallest)

        return -1 if float('inf') in dist else max(dist)