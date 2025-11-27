class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for s in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    for d in ds:
                        nx, ny = x + d[0], y + d[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            dp[s][x][y] += 1
                        else:
                            dp[s][x][y] = (dp[s][x][y] + dp[s - 1][nx][ny]) % (
                                10**9 + 7
                            )
        return dp[N][i][j]


if __name__ == "__main__":
    m = 2
    n = 2
    N = 2
    i = 0
    j = 0
    res = Solution().findPaths(m, n, N, i, j)
    print(res)

    m = 1
    n = 3
    N = 3
    i = 0
    j = 1
    res = Solution().findPaths(m, n, N, i, j)
    print(res)
