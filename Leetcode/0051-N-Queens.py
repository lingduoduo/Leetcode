from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(k, j):
            for i in range(k):
                if board[i] - j == 0 or k - i == abs(board[i] - j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n:
                res.append(valuelist)
                return

            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = "." * n
                    dfs(depth + 1, valuelist + [s[:i] + "Q" + s[i + 1 :]])

        board = [-1 for i in range(n)]
        res = []
        dfs(0, [])
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def dfs(row, diagonals, anti_diagonals, cols, state):
            if row == n:
                res.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if (
                    col in cols
                    or curr_diagonal in diagonals
                    or curr_anti_diagonal in anti_diagonals
                ):
                    continue

                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"
                dfs(row + 1, diagonals, anti_diagonals, cols, state)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        res = []
        empty_board = [["."] * n for _ in range(n)]
        dfs(0, set(), set(), set(), empty_board)
        return res


if __name__ == "__main__":
    res = Solution().solveNQueens(n=4)
    print(res)
