class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        self.dp = [[float('inf')] * m for _ in range(n)]
        return self.path(n - 1, m - 1, grid)
    
    def path(self, x, y, grid):
        print([x, y, grid])
        if x == 0 and y == 0:
            self.dp[x][y] = grid[x][y]
        elif x < 0 or y < 0:
            return float('inf')
        elif self.dp[x][y] != float('inf'):
            return self.dp[x][y]
        else:
            self.dp[x][y] = grid[x][y] + min(self.path(x - 1, y, grid), self.path(x, y - 1, grid))
        
        return self.dp[x][y]
    #
    #
    #     n = len(grid)
    #     if n == 0:
    #         return 0
    #     m = len(grid[0])
    #
    #     self.dp = [[float('inf')] * (1 + m) for _ in range(1 + n)]
    #
    #     return self.path(n, m, grid)
    #
    # def path(self, x, y, grid):
    #     if x <= 0 or y <= 0:
    #         return self.dp[x][y]
    #     if x == 1 and y == 1:
    #         self.dp[x][y] = grid[x-1][y-1]
    #     else:
    #         left =  self.path(x, y - 1, grid)
    #         self.dp[x][y] = min(self.dp[x][y], grid[x - 1][y - 1] + left)
    #         up = self.path(x - 1, y, grid)
    #         self.dp[x][y] = min(self.dp[x][y], grid[x-1][y-1] + up)
    #     return self.dp[x][y]


if __name__ == '__main__':
    input = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = Solution().minPathSum(input)
    print(result)
