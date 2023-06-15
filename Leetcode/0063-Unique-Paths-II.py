# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         n = len(obstacleGrid)
#         if n == 0:
#             return 0
#         m = len(obstacleGrid[0])

#         self.dp = [[0] * (1 + m) for _ in range(1 + n)]

#         return self.path(n, m, obstacleGrid)

#     def path(self, x, y, obstacleGrid):
#         if x <= 0 or y <= 0:
#             return 0
#         if x == 1 and y == 1:
#             return 1 - obstacleGrid[0][0]
#         if self.dp[x][y] != 0:
#             return self.dp[x][y]
#         if obstacleGrid[x - 1][y - 1] == 1:
#             return 0
#         else:
#             self.dp[x][y] = self.path(x - 1, y, obstacleGrid) + self.path(x, y - 1, obstacleGrid)
#         return self.dp[x][y]


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
