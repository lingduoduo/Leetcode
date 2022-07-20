class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y, index):
            q = [(x, y)]
            visit = {(x, y)}
            while q:
                curx, cury = q.pop()
                grid[curx][cury] = index
                for dx, dy in directions:
                    tx, ty = curx + dx, cury + dy
                    if 0 <= tx < n and 0 <= ty < n and grid[tx][ty] == 1:
                        q.append((tx, ty))
                        visit.add((tx, ty))
            return len(visit)

        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        area = {}
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1

        res = max(area.values() or [0])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    tmp = set()
                    for dx, dy in directions:
                        tx, ty = i + dx, j + dy
                        if 0 <= tx < n and 0 <= ty < n and grid[tx][ty] > 1:
                            tmp.add(grid[tx][ty])
                    res = max(res, 1 + sum(area[t] for t in tmp))
        return res