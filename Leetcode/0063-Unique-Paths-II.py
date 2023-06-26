class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0] * (1 + m) for _ in range(1 + n)]
        dp[1][1] = 1 - obstacleGrid[0][0]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1 and j == 1:
                    dp[i][j] = 1 - obstacleGrid[0][0]
                elif obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


if __name__ == "__main__":
    input = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result = Solution().uniquePathsWithObstacles(input)
    print(result)
