from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        que = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        res = 0
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + x, j + y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        que.append((nx, ny))
                        fresh -= 1
            res += 1
        return res if fresh == 0 else -1