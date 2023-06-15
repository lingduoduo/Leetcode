class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if a == b:
                    if i >= 1 and j >= 1:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                    else:
                        dp[i][j] = 1
        return dp[-1][-1]
