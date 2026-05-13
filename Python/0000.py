from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        heap = []
        heapq.heappush(heap, (1, 0, 0))
        grid[0][0] = 1

        while heap:
            step, i, j = heapq.heappop(heap)
            if i == n - 1 and j == n - 1:
                return step
            
            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    heapq.heappush(heap, (step + 1, nx, ny))
        return -1

if __name__ == "__main__":
    print(Solution().shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))