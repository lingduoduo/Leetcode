class Solution(object):
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for i in range(n)]

        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, n):
            for j in range(1, m):
                if dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
        return dp[-1][-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


if __name__ == "__main__":
    input = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = Solution().minPathSum(input)
    print(result)
