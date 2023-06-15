from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    startx = i
                    starty = j
                    break

        res = 0
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for dx, dy in dirs:
            x = startx
            y = starty
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == "B":
                    break
                if board[x][y] == "p":
                    res += 1
                    break
                x = x + dx
                y = y + dy
        return res


if __name__ == "__main__":
    res = Solution().numRookCaptures(
        board=[
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", "R", ".", ".", ".", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
    print(res)
