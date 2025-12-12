import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            distance, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return distance
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    new_distance = max(distance, abs(heights[i][j] - heights[x][y]))
                    if new_distance < dist[x][y]:
                        dist[x][y] = new_distance
                        heapq.heappush(pq, (new_distance, x, y))
