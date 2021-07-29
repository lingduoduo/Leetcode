class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
    ###    for x in range(len(board)):
    ###        for y in range(len(board[0])):
    ###            if self.search(board, word, x, y, 0):
    ###                return True
        
    ###    return False
    
    ###def search(self, board, word, i, j, d):
    ###    if d == len(word):
    ###        return True
        
    ###    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
    ###        return False
        
    ###    if board[i][j] != word[d]:
    ###        return False
        
    ###    board[i][j] = board[i][j].swapcase()
    ###    result = self.search(board, word, i + 1, j, d + 1) or \
    ###             self.search(board, word, i - 1, j, d + 1) or \
    ###             self.search(board, word, i, j + 1, d + 1) or \
    ###             self.search(board, word, i, j - 1, d + 1)
    ###    board[i][j] = board[i][j].swapcase()
        
    ###    return result

class Solution(object):
    def exist(self, board, word):
            for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):
                    return True
        return False

    def helper(board, i, j, word, wordinx):
        if wordinx == len(word):
            return True

        if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1:
            return False

        if word[wordinx] != board[i][j]:
            return False

        board[i][j] = "#"    
        found = self.helper(board, i+1, j, word, wordinx+1) \
        or self.helper(board, i-1, j, word, wordinx+1) \
        or self.helper(board, i, j-1, word, wordinx+1) \
        or self.helper(board, i, j+1, word, wordinx+1) 
        board[i][j] = word[wordinx]

        return found


from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtracking(board, word, 0, i, j):
                    return True
        return False

    def backtracking(self, board, word, idx, r, c):
        if idx == len(word):
            return True

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[idx] or self.visited[r][c]:
            return False
        
        self.visited[r][c] = True
        paths = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for p in paths:
            if self.backtracking(board, word, idx+1, r + p[0], c + p[1]):
                return True
        self.visited[r][c] = False

        return False

if __name__ == '__main__':
    res = Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED")
    print(res)

