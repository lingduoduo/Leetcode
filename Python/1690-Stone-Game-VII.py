class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + stones[i]
        dp = [[0] * n for _ in range(n)]
        for c in range(2, n + 1):
            l = 0
            r = l + c - 1
            while r < n:
                dp[l][r] = max(
                    s[r + 1] - s[l + 1] - dp[l + 1][r], s[r] - s[l] - dp[l][r - 1]
                )
                l += 1
                r += 1
        return dp[0][n - 1]


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        cache = [[float("inf")] * n for _ in range(n)]

        @lru_cache(None)
        def dp(l, r, s):
            if l >= r:
                return 0
            if cache[l][r] == float("inf"):
                cache[l][r] = max(
                    s - stones[r] - dp(l, r - 1, s - stones[r]),
                    s - stones[l] - dp(l + 1, r, s - stones[l]),
                )
            return cache[l][r]

        return dp(0, n - 1, sum(stones))
