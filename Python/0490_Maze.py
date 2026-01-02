from typing import List


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        m, n = len(maze), len(maze[0])
        visit = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        stack = [start]
        while stack:
            curx, cury = stack.pop()
            if [curx, cury] == destination:
                return True
            for dirx, diry in directions:
                tx, ty = curx, cury
                while (
                    0 <= tx + dirx < m
                    and 0 <= ty + diry < n
                    and not maze[tx + dirx][ty + diry]
                ):
                    tx, ty = tx + dirx, ty + diry
                if (tx, ty) not in visit:
                    visit.add((tx, ty))
                    stack.append((tx, ty))
        return False

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n = len(maze)
        m = len(maze[0])
        visited = set()
        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m and maze[x][y] == 0):
                return False
            if [x, y] == destination: return True      
            if (x, y) in visited: return False
            visited.add((x, y))
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x, y
                # roll until hitting wall
                while 0 <= nx + dx < n and 0 <= ny + dy < m and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                # stop position (nx, ny)
                if dfs(nx, ny):
                    return True
            return False
        return dfs(start[0], start[1])