from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(i, j))
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(grid, i, j))
        return res

    def dfs(self, grid, i, j):
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[0])
            or grid[i][j] == 0
            or (i, j) in self.visited
        ):
            return 0

        grid[i][j] == 0
        self.visited.add((i, j))
        return (
            1
            + self.dfs(grid, i + 1, j)
            + self.dfs(grid, i - 1, j)
            + self.dfs(grid, i, j + 1)
            + self.dfs(grid, i, j - 1)
        )


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(grid, i, j):
            if (
                    i < 0
                    or i >= len(grid)
                    or j < 0
                    or j >= len(grid[0])
                    or grid[i][j] == 0
                    or (i, j) in visited
            ):
                return 0

            grid[i][j] == 0
            visited.add((i, j))
            return  1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j))
        return res

