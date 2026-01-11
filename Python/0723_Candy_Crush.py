from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        while True:
            stable = True
            crushable = set()
            # 1. check for horizontal crushables
            for x in range(m):
                for y in range(n - 2):
                    if board[x][y] == board[x][y + 1] == board[x][y + 2] != 0:
                        stable = False
                        crushable.update([(x, y), (x, y + 1), (x, y + 2)])

            # 2. check for vertical crushables
            for x in range(m - 2):
                for y in range(n):
                    if board[x][y] == board[x + 1][y] == board[x + 2][y] != 0:
                        stable = False
                        crushable.update([(x, y), (x + 1, y), (x + 2, y)])

            # 5. if no candies were crushed, we're done
            if stable:
                return board

            # 3. crush the candies
            for x, y in crushable:
                board[x][y] = 0

            # 4. let the candies "fall"
            for y in range(n):
                offset = 0
                for x in range(m - 1, -1, -1):  # loop through column backward
                    k = x + offset
                    if (
                        x,
                        y,
                    ) in crushable:  # this will help us put items at bottom of the board
                        offset += 1
                    else:
                        board[k][y] = board[x][y]  # notice the use of k
                # now that all items have been copied to their right spots, place zero's appropriately at the top of the board
                for x in range(offset):
                    board[x][y] = 0

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        while True:
            mark = [[False] * n for _ in range(m)]
        
            for r in range(m):
                for c in range(n - 2):
                    v = board[r][c]
                    if v != 0 and v == board[r][c + 1] == board[r][c + 2]:
                        mark[r][c] = mark[r][c + 1] = mark[r][c + 2] = True
            
            for r in range(m - 2):
                    for c in range(n):
                        v = board[r][c]
                        if v != 0 and v == board[r + 1][c] == board[r + 2][c]:
                            mark[r][c] = mark[r + 1][c] = mark[r + 2][c] = True
            
            if not any(any(row) for row in mark):
                return board
            
            for r in range(m):
                for c in range(n):
                    if mark[r][c]:
                        board[r][c] = 0
        
            for c in range(n):
                write = m - 1
                for r in range(m - 1, -1, -1):
                    if board[r][c] != 0:
                        board[write][c] = board[r][c]
                        write -= 1
                for r in range(write, -1, -1):
                    board[r][c] = 0


