class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if fresh == 0:
            return 0

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                for d in directions:
                    dx, dy = x + d[0], y + d[1]
                    if dx < 0 or dx >= m or dy < 0 or dy >= n or grid[dx][dy] != 1:
                        continue
                    grid[dx][dy] = 2
                    q.append((dx, dy))
                    fresh -= 1
            step += 1
        if fresh != 0:
            return -1
        return step - 1
