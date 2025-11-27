class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        nrow, ncol = len(board), len(board[0])

        prev = copy.deepcopy(board)
        for i in range(nrow):
            for j in range(ncol):
                live = self.getLiveNeighbors(prev, i, j)

                if prev[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1

    def getLiveNeighbors(self, prev, x, y):
        nrow, ncol = len(prev), len(prev[0])

        cnt = 0
        shift = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for tup in shift:
            dx, dy = tup[0], tup[1]
            if 0 <= x + dx < nrow and 0 <= y + dy < ncol and prev[x + dx][y + dy] == 1:
                cnt += 1
        return cnt


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return 0
            return res[i][j]

        m = len(board)
        n = len(board[0])
        res = copy.deepcopy(board)
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dir in [
                    [-1, -1],
                    [-1, 0],
                    [-1, 1],
                    [0, -1],
                    [0, 1],
                    [1, -1],
                    [1, 0],
                    [1, 1],
                ]:
                    cnt += check(i + dir[0], j + dir[1])
                if res[i][j] == 1 and cnt < 2:
                    board[i][j] = 0
                elif res[i][j] == 1 and cnt in [2, 3]:
                    board[i][j] = 1
                elif res[i][j] == 1 and cnt > 3:
                    board[i][j] = 0
                if res[i][j] == 0 and cnt == 3:
                    board[i][j] = 1


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## RC ##
        ## APPRAOCH : IN-PLACE MANIPULATION ##
        #  when the value needs to be updated, we donot just change  0 to 1 / 1 to 0 but we do in increments and decrements of 2. (table explains)
        ##   previous value state change  current state   current value
        ##   0              no change     dead            0
        ##   1              no change     live            1
        ##   0              changed (+2)  live            2
        ##   1              changed (-2)  dead            -1

        ## TIME COMPLEXITY : O(MxN) ##
        ## SPACE COMPLEXITY : O(1) ##

        directions = [
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0  # live neighbors count
                for x, y in directions:  # check and count neighbors in all directions
                    if (
                        (i + x < len(board) and i + x >= 0)
                        and (j + y < len(board[0]) and j + y >= 0)
                        and abs(board[i + x][j + y]) == 1
                    ):
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):  # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:  # Rule 4
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if (board[i][j] > 0) else 0
        return board
