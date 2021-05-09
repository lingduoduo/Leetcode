class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        res = 0
        dp = [[N for _ in range(N)] for _ in range(N)]
        s = set()
        for mine in mines:
            dp[mine[0]][mine[1]] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j in range(N):
                l = l + 1 if dp[i][j] else 0
                r = r + 1 if dp[j][i] else 0
                u = u + 1 if dp[i][N - 1 -j] else 0
                d = d + 1 if dp[N - 1 - j][i] else 0
                dp[i][j] = min(dp[i][j], l)
                dp[j][i] = min(dp[j][i], r)
                dp[i][N - 1 - j] = min(dp[i][N -  1 - j], u)
                dp[N - 1 - j][i] = min(dp[N - 1 - j][i], d)
        for i in range(N):
            for j in range(N):
                res = max(res, dp[i][j])
        return res 