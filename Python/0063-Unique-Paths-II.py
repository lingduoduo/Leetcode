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


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)  # 网格的行数
        n = len(obstacleGrid[0])  # 网格的列数

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            # 如果起点或终点有障碍物，直接返回0
            return 0

        dp = [[0] * n for _ in range(m)]  # 创建一个二维列表用于存储路径数

        # 设置起点的路径数为1
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # 计算第一列的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # 计算第一行的路径数
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # 计算其他位置的路径数
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]  # 返回终点的路径数


if __name__ == "__main__":
    input = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result = Solution().uniquePathsWithObstacles(input)
    print(result)
