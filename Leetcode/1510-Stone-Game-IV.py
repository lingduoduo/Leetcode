class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (1+n)
        for i in range(1+n):
            j = 1
            while j * j <= i:
                if not dp[i - j*j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]
        