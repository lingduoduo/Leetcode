class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0
        row = [0] * m
        col = [0] * m

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res += 1
                    row[i] = max(row[i], grid[i][j])
                    col[j] = max(col[j], grid[i][j])
        res += sum(row)
        res += sum(col)
        return res 