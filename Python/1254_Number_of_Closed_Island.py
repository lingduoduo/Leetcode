class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        position = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(x, y):
            grid[x][y] = 1   # mark visited land
            for i, j in position:
                nx = x + i
                ny = y + j
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                    dfs(nx, ny)

        n = len(grid)
        m = len(grid[0])

        # 1. Flood land connected to borders (not closed islands)
        for i in range(n):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][m - 1] == 0:
                dfs(i, m - 1)

        for j in range(m):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[n - 1][j] == 0:
                dfs(n - 1, j)

        # 2. Count remaining 0-regions as closed islands
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    count += 1     # one closed island found
                    dfs(i, j)      # mark whole island

        return count