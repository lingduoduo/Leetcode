from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        q = deque()

        # All water cells start from height 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    q.append((i, j))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS expands from water to land
        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    q.append((nx, ny))

        return heights