class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # Manhattan distance helper
        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        in_mst = [False] * n          # whether point i is already in the tree
        min_edge = [math.inf] * n     # min cost edge to connect each point to MST
        min_edge[0] = 0               # start from point 0 with cost 0
        res = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not in_mst[i] and (u == -1 or min_edge[i] < min_edge[u]):
                    u = i

            in_mst[u] = True
            res += min_edge[u]
            for v in range(n):
                if not in_mst[v]:
                    w = dist(u, v)
                    if w < min_edge[v]:
                        min_edge[v] = w

        return res
