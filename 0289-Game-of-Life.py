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
        shift = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
        ]
        for tup in shift:
            dx, dy = tup[0], tup[1]
            if 0 <= x+dx < nrow and 0<=y+dy<ncol and prev[x+dx][y+dy]==1:
                cnt += 1
        return cnt
        