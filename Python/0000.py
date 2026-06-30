from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if not (0 <= i < m and 0 <= j < n):
                return False

            if board[i][j] == word[idx]:
                return False

            tmp = board[i][j]
            board[i][j] = ""

            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = i + dx, j + dy
                if dfs(nx, ny, idx + 1):
                    board[i][j] = tmp
                    return True

            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False


if __name__ == "__main__":
    res = Solution().subsets(nums=[1, 2, 3])
    print(res)
