from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
   

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, grp):
            nonlocal cur
            cur += 1
            grid[x][y] = grp

            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny)

        d = defaultdict(dict)
        grp = 2
        for i in range(m):
            for j in range(n):
                cur = 0
                if grid[i][j] == 1:
                    dfs(i, j, grp)
                    d[grp] = cur
                    grp += 1

        res = 0
        for i in range(m):
            for j in range(n):
                cur = 0
                visited = set()
                if grid[i][j] == 0:
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:   
                        nx, ny = i + dx, j + dy
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            cur += d[grid[nx][ny]]
                    res = max(res, cur)
        return res
                
                    

if __name__ == "__main__":
    print(Solution().numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))