import collections
import heapq


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        d = collections.defaultdict(list)
        for s, e, p in flights:
            d[s].append((e, p))

        self.res = [float("inf")]
        visited = set()
        self.dfs(n, visited, d, src, dst, K + 1, 0)
        if min(self.res) == float("inf"):
            return -1
        else:
            return min(self.res)

    def dfs(self, n, visited, d, src, dst, K, path):
        if src == dst:
            self.res.append(path)
            return True

        if K == 0:
            return

        for end, price in d[src]:
            if end in visited:
                continue
            if path + price > min(self.res):
                continue
            visited.add(src)
            self.dfs(n, visited, d, end, dst, K - 1, path + price)
            visited.remove(src)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(k + 1):
            nxt = dist[:]  
            changed = False
            for u, v, w in flights:
                if dist[u] == float("inf"):
                    continue
                cand = dist[u] + w
                if cand < nxt[v]:
                    nxt[v] = cand
                    changed = True

            dist = nxt
            if not changed:  # early exit if no relaxation happened
                break

        return -1 if dist[dst] == float("inf") else dist[dst]


if __name__ == "__main__":
    n = 3
    edges = [[0, 2, 500], [0, 1, 100], [1, 2, 100]]
    src = 0
    dst = 2
    k = 1
    res = Solution().findCheapestPrice(n, edges, src, dst, k)
    print(res)
