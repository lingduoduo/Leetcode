import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        heap = [(-grid[0][0], 0, 0)]
        res = -grid[0][0]
        while heap:
            v, i, j = heapq.heappop(heap)
            res = max(res, v)
            if i == n - 1 and j == m - 1:
                return -res
            grid[i][j] = -1
            for ii, jj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ii < n and 0 <= jj < m and grid[ii][jj] >= 0:
                    heapq.heappush(heap, (-grid[ii][jj], ii, jj))

