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

    # def dfs(self, graph, src, dst, k, cost, visited, ans):
    #     if src == dst:
    #         ans[0] = cost
    #         return
    #     if k == 0:
    #         return
    #     for v, e in graph[src].items():
    #         if visited[v]: continue
    #         if cost + e > ans[0]: continue
    #         visited[v] = 1
    #         self.dfs(graph, v, dst, k - 1, cost + e, visited, ans)
    #         visited[v] = 0


if __name__ == "__main__":
    n = 3
    edges = [[0, 2, 500], [0, 1, 100], [1, 2, 100]]
    src = 0
    dst = 2
    k = 1
    res = Solution().findCheapestPrice(n, edges, src, dst, k)
    print(res)
