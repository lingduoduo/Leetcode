class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = [[0 for _ in s] for _ in s]

        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(1 + dp[i][j - 1], 1 + dp[i + 1][j], 2 + dp[i + 1][j - 1])
        # print(dp)
        return dp[0][-1] <= k