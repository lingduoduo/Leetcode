from typing import List

class Solution:
    def min_cost_ii(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        m = len(costs)
        n = len(costs[0])

        dp = [[float("inf")] * n for _ in range(m)]

        for j in range(n):
            dp[0][j] = costs[0][j]
        
        for i in range(m):
            for j in range(n):
                for k in range(n):
                    if j == k: 
                        continue
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i][j])
        
        return min(dp[m - 1])
