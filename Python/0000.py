from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.dia = 0
        self.off_dia = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.dia += 1
            if row + col == self.n:
                self.dia += 1
            if self.row == self.n or self.col == self.n or self.dia == self.n or self.off_dia == self.n:
                return 1
            else:
                return 0
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.dia -= 1
            if row + col == self.n:
                self.dia -= 1
            if self.row == self.n or self.col == self.n or self.dia == self.n or self.off_dia == self.n:
                return 1
            else:
                return 2


if __name__ == "__main__":
    res = Solution().monotoneIncreasingDigits(n = 668841)
    print(res)
