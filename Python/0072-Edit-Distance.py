from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)

        @lru_cache(None)
        def dp(i, j):
            if i >= w1:
                return w2 - j  # word1 used up, so all inserts
            if j >= w2:
                return w1 - i  # word2 used up, so all deletes
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)  # letters match, so no operation

            return (
                min(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1)) + 1
            )  # insert, delete, replace

        return dp(0, 0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[-1][-1]
