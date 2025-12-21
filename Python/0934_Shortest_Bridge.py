from typing import List, Tuple
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 1) find any cell of the first island
        si = sj = -1
        found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    si, sj = i, j
                    found = True
                    break
            if found:
                break

        # 2) DFS to collect all cells in the first island
        stack: List[Tuple[int, int]] = [(si, sj)]
        visited = {(si, sj)}  # cells already in island or already expanded in BFS

        while stack:
            i, j = stack.pop()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited:
                    stack.append((x, y))      # <-- tuple, not list
                    visited.add((x, y))

        # 3) BFS expansion layer by layer from the first island until hitting the second
        q = deque(visited)
        steps = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                        if grid[x][y] == 1:
                            return steps
                        visited.add((x, y))
                        q.append((x, y))
            steps += 1

        return -1
