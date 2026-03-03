from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pac = set()
        atl = set()

        def dfs(i, j, seen):
            seen.add((i, j))
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    if heights[ni][nj] >= heights[i][j]:
                        dfs(ni, nj, seen)

        # Pacific
        for j in range(n):
            dfs(0, j, pac)
        for i in range(m):
            dfs(i, 0, pac)

        # Atlantic: 
        for j in range(n):
            dfs(m - 1, j, atl)
        for i in range(m):
            dfs(i, n - 1, atl)

        return [[i, j] for (i, j) in pac & atl]