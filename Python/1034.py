from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        old = grid[row][col]

        def dfs(x, y):
            visited.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == old and (nx, ny) not in visited:
                    dfs(nx, ny)

        dfs(row, col)

        for (i, j) in list(visited):
            is_border = (i == 0 or i == m - 1 or j == 0 or j == n - 1)
            if not is_border:
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if (ni, nj) not in visited:
                        is_border = True
                        break
            if is_border:
                grid[i][j] = color

        return grid