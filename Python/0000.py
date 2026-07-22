from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq
import random


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum([row.count("X") for row in board])
        o_count = sum([row.count("O") for row in board])
        if x_count not in (o_count, o_count + 1):
            return False

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

        x_wins = wins("X")
        o_wins = wins("O")
        if x_wins and o_wins:
            return False

        if x_wins and x_count != o_count + 1:
            return False

        if o_wins and x_count != o_count:
            return False

        return True


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

        i = 0
        for row, col in moves:
            if i % 2 == 0:
                board[row][col] = "X"
            else:
                board[row][col] = "O"
            i += 1
            print(board)

        if wins("X"):
            return "A"
        elif wins("O"):
            return "B"
        else:
            return "Draw"


if __name__ == "__main__":
    res = Solution().tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]])
    print(res)
