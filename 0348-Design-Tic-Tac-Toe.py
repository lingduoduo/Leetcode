class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[' ']*n for i in range(n)]       
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            mark = 'X'
        else:
            mark = 'O'
            
        self.grid[row][col] = mark
        # check wining condition
        # check if the row has the same mark
        n = len(self.grid)
        sum_of_row = sum([self.grid[row][c] == mark for c in range(n)])
        sum_of_col = sum([self.grid[r][col]== mark for r in range(n)])
        sum_of_left_d = sum([self.grid[i][i] == mark for i in range(n)])
        sum_of_right_d = sum([self.grid[i][n-1-i] == mark for i in range(n)])
        if sum_of_row == n or sum_of_col == n or sum_of_left_d== n or sum_of_right_d == n:
            return player        
        else:
            return 0