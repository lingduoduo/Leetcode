from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pq = [(grid[0][0], 0, 0)]     # (time_so_far, x, y)
        visited = {(0, 0)}

        while pq:
            t, x, y = heapq.heappop(pq)
            if (x, y) == (n - 1, n - 1):
                return t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    nt = max(t, grid[nx][ny])  # time needed to enter neighbor
                    heapq.heappush(pq, (nt, nx, ny))
