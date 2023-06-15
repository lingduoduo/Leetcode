class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False] * n for _ in range(m)]
        q_visited = [[False] * n for _ in range(m)]
        for i in range(m):
            self.dfs(matrix, p_visited, m, n, i, 0)
            self.dfs(matrix, q_visited, m, n, i, n - 1)
        for j in range(n):
            self.dfs(matrix, p_visited, m, n, 0, j)
            self.dfs(matrix, q_visited, m, n, m - 1, j)
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] == q_visited[i][j] == 1:
                    res.append([i, j])
        return res

    def dfs(self, matrix, visited, m, n, i, j):
        visited[i][j] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            if (
                x < 0
                or x >= m
                or y < 0
                or y >= n
                or visited[x][y]
                or matrix[x][y] < matrix[i][j]
            ):
                continue
            self.dfs(matrix, visited, m, n, x, y)


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if matix is None:
            return []

        m = len(matrix)
        n = len(matrix[0])
        stack = []
        for i in range(m):
            stack.append((i, 0))
        for i in range(n):
            stack.append((0, i))
        pac = self.dfs(matrix, stack)

        stack = []
        for i in range(m):
            stack.append((i, n - 1))
        for i in range(n):
            stack.append((m - 1, i))
        atl = self.dfs(matrix, stack)

        res = pac.intersection(atl)
        return [list(x) for x in res]

    def dfs(self, matrix, q):
        m = len(matrix)
        n = len(matrix[0])
        res = set([])
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        while len(q) > 0:
            curx, cury = q.pop()
            ret.add((curx, cury))
            height = matrix[curx][cury]
            for dirx, diry in directions:
                tmpx, tmpy = dirx + curx, diry + cury
                if 0 <= tmpx < m and 0 <= tmpy < n and matrix[tmpx][tmpy] >= height:
                    if (tmpx, tmpy) not in ret:
                        q.append((tmpx, tmpy))
                        ret.add((tmpx, tmpy))
        return res
