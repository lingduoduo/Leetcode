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
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        # (cost, node, stops)
        queue = deque([(0, src, 0)])
        
        # best[node][stops] = min cost
        best = dict()
        res = float("inf")

        while queue:
            cost, node, stops = queue.popleft()

            if node == dst:
                res = min(res, cost)
                continue

            if stops > k:
                continue

            for nxt, price in graph[node]:
                new_cost = cost + price

                if new_cost >= res:
                    continue

                if (nxt, stops + 1) not in best or new_cost < best[(nxt, stops + 1)]:
                    best[(nxt, stops + 1)] = new_cost
                    queue.append((new_cost, nxt, stops + 1))

        return -1 if res == float("inf") else res


if __name__ == "__main__":
    n = 3
    edges = [[0, 2, 500], [0, 1, 100], [1, 2, 100]]
    src = 0
    dst = 2
    k = 1
    res = Solution().findCheapestPrice(n, edges, src, dst, k)
    print(res)
