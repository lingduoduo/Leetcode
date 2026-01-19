class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def checker(mat):
            # must be 1..9 exactly once
            vals = [mat[i][j] for i in range(3) for j in range(3)]
            if set(vals) != set(range(1, 10)):
                return False

            row = [0] * 3
            col = [0] * 3
            dig = [0] * 2

            for i in range(3):
                row[i] = sum(mat[i])

            for j in range(3):
                col[j] = sum(mat[i][j] for i in range(3))

            for i in range(3):
                dig[0] += mat[i][i]
                dig[1] += mat[i][2 - i]

            return len(set(row + col + dig)) == 1

        res = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                mat = [row[j:j+3] for row in grid[i:i+3]]  # correct 3x3
                if checker(mat):
                    res += 1
        return res