class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in reversed(range(n)):
            dp[i][i] = 1
            for j in range(i + 1, n):
                print([i, j])
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == "__main__":
    s = "bbbab"
    res = Solution().longestPalindromeSubseq(s)
    print(res)
