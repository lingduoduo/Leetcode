class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Dictionary for memoization
        memo = {}

        def uniqueSubsequences(i, j):
            m, n = len(s), len(t)
            # Base case
            if i == m or j == n or m - i < n - j:
                return int(j == len(t))
            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i, j]
            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)
            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)
            # Cache the answer and return
            memo[i, j] = ans
            return ans

        return uniqueSubsequences(0, 0)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


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
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1
                    )
        return dp[-1][-1]
