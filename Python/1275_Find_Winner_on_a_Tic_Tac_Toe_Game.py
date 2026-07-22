from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[" "] * 3 for _ in range(3)]

        def wins(player: str) -> bool:
            # Check rows.
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True

            # Check columns.
            for j in range(3):
                if all(board[i][j] == player for i in range(3)):
                    return True

            # Check main diagonal.
            if all(board[i][i] == player for i in range(3)):
                return True

            # Check anti-diagonal.
            if all(board[i][2 - i] == player for i in range(3)):
                return True

            return False

        for i, (r, c) in enumerate(moves):
            board[r][c] = "X" if i % 2 == 0 else "O"

        if wins("X"):
            return "A"

        if wins("O"):
            return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"
