from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        X = 0
        Y = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    X += 1
                if board[i][j] == "O":
                    Y += 1

        if not (X == Y or X == Y + 1):
            return False
        if X == Y and self.win(board, "X"):
            return False
        if X == Y + 1 and self.win(board, "O"):
            return False

        return True

    def win(self, board, cha):
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == cha:
                return True

        for j in range(len(board[0])):
            if board[0][j] == board[1][j] == board[2][j] == cha:
                return True

        if board[0][0] == board[1][1] == board[2][2] == cha:
            return True

        if board[0][2] == board[1][1] == board[2][0] == cha:
            return True

        return False


if __name__ == "__main__":
    board = ["XXX", "   ", "OOO"]
    res = Solution().validTicTacToe(board)
    print(res)
