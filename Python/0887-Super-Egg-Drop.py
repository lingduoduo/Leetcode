class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for m in range(1, n + 1):
            for i in range(1, k + 1):
                dp[m][i] = dp[m - 1][i - 1] + dp[m - 1][i] + 1
            if dp[m][k] >= n:
                return m
