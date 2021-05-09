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


class Solution(object):
    def exist(self, board, word):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.dfs(board, word, x, y, 0):
                    return True
        return False
    
    def dfs(self, board, word, x, y, i):
        if i == len(word):
            return True
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] = "#"
        found =  self.dfs(board, word, x + 1, y, i + 1) or self.exit(board, word, x, y + 1, i + 1) or self.exit(board, word, x - 1, y, i + 1) or self.exit(board, word, x, y - 1, i + 1)
        board[y][x] = word[i]
        return found
