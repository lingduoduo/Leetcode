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
        n, m = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs_explore(r, c):
            if (r < 0 or r >= n or c < 0 or c >= m or board[r][c] != 'O'):
                return

            board[r][c] = 'D'
            for dr, dc in dirs:
                dfs_explore(r + dr, c + dc)

        for r in range(n):
            if board[r][0] == 'O':
                dfs_explore(r, 0)
            if board[r][m - 1] == 'O':
                dfs_explore(r, m - 1)

        for c in range(m):
            if board[0][c] == 'O':
                dfs_explore(0, c)
            if board[n - 1][c] == 'O':
                dfs_explore(n - 1, c)

        # Flip all 'O' to 'X' unless they've been marked as 'D'
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'  # Flip
                elif board[row][col] == 'D':
                    board[row][col] = 'O'  # Restore
