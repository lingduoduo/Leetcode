class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 

        def dfs(i, j):
            nonlocal res
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 

            grid[i][j] = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
                    dfs(i, j)
        return sum(sum(row) for row in grid)
        