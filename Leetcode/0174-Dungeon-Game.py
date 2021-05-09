class Solution:
    def calculateMinimumHP(self, dungeon):
        
        n, m = len(dungeon), len(dungeon[0])  ###初始化dp, n, m 分别代表着 行 和 列
        dp = [[0] * m for _ in range(n)]
        dp[n - 1][m - 1] = max(1 - dungeon[n - 1][m - 1], 1)
        
        for i in range(n - 2, -1, -1):  ###最后一列
            dp[i][m - 1] = max(dp[i + 1][m - 1] - dungeon[i][m - 1], 1)
        
        for j in range(m - 2, -1, -1):  ###最后一行
            dp[n - 1][j] = max(dp[n - 1][j + 1] - dungeon[n - 1][j], 1)
        
        for i in range(n - 2, -1, -1):  ###倒着计算
            for j in range(m - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]), 1)
        return dp[0][0]

if __name__ == '__main__':
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    ###dungeon = [[100]]
    solu = Solution()
    print(solu.calculateMinimumHP(dungeon))
