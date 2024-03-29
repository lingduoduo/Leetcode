from typing import List


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return 0
        n = len(grid)
        m = len(grid[0])
        area = 0
        conn = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area += 1
                    if i > 0 and grid[i - 1][j] == 1:
                        conn += 1
                    if i < n - 1 and grid[i + 1][j] == 1:
                        conn += 1
                    if j > 0 and grid[i][j - 1] == 1:
                        conn += 1
                    if j < m - 1 and grid[i][j + 1] == 1:
                        conn += 1
        return area * 4 - conn


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(grid):
            for j in range(grid[0]):
                if grid[i][j] == 1:
                    result += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        result -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        result -= 2
        return result
