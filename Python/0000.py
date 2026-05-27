from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def dfs(x, y):
            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                return 
            if board[nx][ny] != "E":
                return 
            
            count = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (1, -1)(1, 1), (-1, -1), (-1, 0), (-1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == "M":
                        count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = "B"
                dfs(nx, ny)

        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        elif board[x][y] == "E":
            dfs(x, y)
            
        return board
    


if __name__ == "__main__":
    res = Solution().updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0])
    print(res)
