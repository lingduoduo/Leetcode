from functools import lru_cache


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

        return min(dp[n - 1])