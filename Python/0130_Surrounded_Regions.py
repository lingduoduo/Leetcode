class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return

        n = len(board[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def dfs(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and board[nx][ny] == "O"
                    and (nx, ny) not in visited
                ):
                    visited.add((nx, ny))
                    board[nx][ny] = "G"
                    dfs(nx, ny)

        for x in range(m):
            for y in range(n):
                if (
                    (x == 0 or x == m - 1 or y == 0 or y == n - 1)
                    and board[x][y] == "O"
                    and (x, y) not in visited
                ):
                    board[x][y] = "G"
                    visited.add((x, y))
                    dfs(x, y)

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "G":
                    board[x][y] = "O"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != "O":
                return

            board[x][y] = "I"

            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "I":
                    board[i][j] = "O"
