from typing import List

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):
                    return True

        return False

    def helper(board, i, j, word, wordinx):
        if wordinx == len(word):
            return True

        if (
            i < 0
            or i > len(board) - 1
            or j < 0
            or j > len(board[0]) - 1
            or word[wordinx] != board[i][j]
        ):
            return False

        board[i][j] = "#"
        found = (
            self.helper(board, i + 1, j, word, wordinx + 1)
            or self.helper(board, i - 1, j, word, wordinx + 1)
            or self.helper(board, i, j - 1, word, wordinx + 1)
            or self.helper(board, i, j + 1, word, wordinx + 1)
        )
        board[i][j] = word[wordinx]
        return found


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtracking(board, word, i, j, 0):
                    return True
        return False

    def backtracking(self, board, word, row, col, idx):
        if len(word) == idx:
            return True

        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[0])
            or board[row][col] != word[size]
            or self.visited[row][col]
        ):
            return False

        self.visited[row][col] = True
        paths = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for path in paths:
            if self.backtracking(board, word, row + path[0], col + path[1], idx + 1):
                return True
        self.visited[row][col] = False
        return False


if __name__ == "__main__":
    res = Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
    print(res)
