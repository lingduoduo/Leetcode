class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        if m == 1 and grid[0][0] == 0:
            return 1

        stack = []
        stack.append((0, 0))
        
        visited = [[0]*n for _ in range(m)]
        visited[0][0] = 1

        directions = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        step = 1
        while stack:
            size = len(stack)
            for i in range(size):
                x, y = stack.pop(0)
                for d in directions:
                    dx, dy = x + d[0], y + d[1]
                    if dx <0 or dx >= m or dy < 0 or dy >= n or grid[dx][dy] == 1 or visited[dx][dy] == 1:
                        continue
                    if dx == n-1 and dy == m-1:
                        return step + 1
                    visited[dx][dy] = 1
                    stack.append((dx, dy))
            step += 1
        return -1
