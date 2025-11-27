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


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(row: int) -> None:
            nonlocal result
            nonlocal chessboard
            if row == n:
                result.append(chessboard[:])  # 棋盘填满，将当前解加入结果集
                return

            for col in range(n):
                if self.isValid(row, col, chessboard):
                    chessboard[row] = (
                        chessboard[row][:col] + "Q" + chessboard[row][col + 1 :]
                    )  # 放置皇后
                    backtracking(row + 1)  # 递归到下一行
                    chessboard[row] = (
                        chessboard[row][:col] + "." + chessboard[row][col + 1 :]
                    )  # 回溯，撤销当前位置的皇后

        result = []  # 存储最终结果的二维字符串数组
        chessboard = ["." * n for _ in range(n)]  # 初始化棋盘
        backtracking(0)  # 回溯求解
        return [["".join(row) for row in solution] for solution in result]  # 返回结果集

    def isValid(self, row: int, col: int, chessboard: List[str]) -> bool:
        # 检查列
        for i in range(row):
            if chessboard[i][col] == "Q":
                return False  # 当前列已经存在皇后，不合法

        # 检查 45 度角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == "Q":
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == "Q":
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1
        return True  # 当前位置合法


if __name__ == "__main__":
    res = Solution().solveNQueens(n=4)
    print(res)
