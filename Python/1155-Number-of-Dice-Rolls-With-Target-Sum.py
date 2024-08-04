class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [
            [0] * (target + 1) for _ in range(d + 1)
        ]  # dp[i][j] i: ith dices j: temp target
        dp[0][0] = 1
        if target < 1 or target > d * f:
            return 0
        for i in range(1, d + 1):
            for j in range(1, f + 1):
                for k in range(j, target + 1):
                    dp[i][k] = (dp[i][k] + dp[i - 1][k - j]) % mod
        return dp[-1][-1]


from functools import lru_cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7

        @lru_cache(maxsize=None)
        def dfs(i, t):
            if i == 0:
                return 1 if t == 0 else 0
            if t > f * i or t < i:
                return 0
            res = 0
            for k in range(1, f + 1):
                res = (res + dfs(i - 1, t - k)) % mod
            return res

        return dfs(d, target)
