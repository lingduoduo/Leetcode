class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp0 = [[0.0] * N for _ in range(N)]
        dp0[r][c] = 1.0
        dirs = [[1, 2], [-1, -2], [1, -2], [-1, 2], [2, 1], [-2, -1], [2, -1], [-2, 1]]
        for k in range(K):
            dp1 = [[0.0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for dir in dirs:
                        x = i + dir[0]
                        y = j + dir[1]
                        if 0 <= x < N and 0 <= y < N:
                            dp1[x][y] += dp0[i][j]
            dp0 = dp1

        tot = sum([num for row in dp0 for num in row])
        return tot / 8**K
