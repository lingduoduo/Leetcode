from typing import List


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        result = 0

        def dfs(grid, x, y):
            if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == "0":
                return
            grid[x][y] = "0"
            dfs(grid, x + 1, y)
            dfs(grid, x - 1, y)
            dfs(grid, x, y + 1)
            dfs(grid, x, y - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                result += 1
        return result


class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j, n, m)
        return res

    def dfs(self, grid, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(grid, i + 1, j, n, m)
        self.dfs(grid, i - 1, j, n, m)
        self.dfs(grid, i, j + 1, n, m)
        self.dfs(grid, i, j - 1, n, m)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            grid[row][col] = "0"
            for direction in directions:
                dx, dy = row + direction[0], col + direction[1]
                if (
                    dx < 0
                    or dx >= len(grid)
                    or dy < 0
                    or dy >= len(grid[0])
                    or grid[dx][dy] == "0"
                ):
                    continue
                dfs(dx, dy)

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    d[i, j] = idx
                    idx += 1

        uf = UnionFind(idx)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i > 0 and grid[i - 1][j] == "1":
                        uf.union(d[i - 1, j], d[i, j])
                    if j > 0 and grid[i][j - 1] == "1":
                        uf.union(d[i, j - 1], d[i, j])
        return uf.groups

        return union.groups


class UnionFind:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]
        self.groups = n

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)

        if x_root == y_root:
            return True

        if self.rank[x_root] > self.rank[y_root]:
            self.parents[y_root] = x_root
            self.rank[x_root] += self.rank[y_root]
        else:
            self.parents[x_root] = y_root
            self.rank[y_root] += self.rank[x_root]
        self.groups -= 1

        return False
