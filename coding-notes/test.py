from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtracking(board, word, 0, i, j):
                    return True
        return False

    def backtracking(self, board, word, idx, r, c):
        if idx == len(word):
            return True

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[idx]:
            return False
        
        curr = board[r][c]
        board[r][c] = ""
        paths = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for p in paths:
            if self.backtracking(board, word, idx+1, r + p[0], c + p[1]):
                return True
        board[r][c] = curr

        return False

if __name__ == '__main__':
    res = Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED")
    print(res)
