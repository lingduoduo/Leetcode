class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.search(board, word, x, y, 0):
                    return True
        
        return False
    
    def search(self, board, word, i, j, d):
        if d == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] != word[d]:
            return False
        
        board[i][j] = board[i][j].swapcase()
        result = self.search(board, word, i + 1, j, d + 1) or \
                 self.search(board, word, i - 1, j, d + 1) or \
                 self.search(board, word, i, j + 1, d + 1) or \
                 self.search(board, word, i, j - 1, d + 1)
        board[i][j] = board[i][j].swapcase()
        
        return result
