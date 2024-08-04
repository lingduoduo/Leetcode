class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j1, j2):
            if i == m - 1:
                return grid[i][j1] + grid[i][j2]
            res = 0
            for d1 in [j1 - 1, j1, j1 + 1]:
                for d2 in [j2 - 1, j2, j2 + 1]:
                    if d1 < d2 and 0 <= d1 < n and 0 <= d2 < n:
                        res = max(res, dfs(i + 1, d1, d2))
            return res + grid[i][j1] + grid[i][j2]

        m, n = len(grid), len(grid[0])
        return dfs(0, 0, n - 1)
