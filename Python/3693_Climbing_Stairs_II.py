class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
        dp = [0] * (n + 1)

        dp[0] = 0
        if n >= 1:
            dp[1] = costs[1] + 1
        if n >= 2:
            dp[2] = min(
                dp[1] + costs[2] + 1,
                dp[0] + costs[2] + 2 ** 2
            )
        if n >= 3:
            dp[3] = min(
                dp[2] + costs[3] + 1,
                dp[1] + costs[3] + 2 ** 2,
                dp[0] + costs[3] + 3 ** 2
            )

        for i in range(4, n + 1):
            dp[i] = min(
                dp[i - 1] + costs[i] + 1,
                dp[i - 2] + costs[i] + 2 ** 2,
                dp[i - 3] + costs[i] + 3 ** 2
            )

        return dp[n]