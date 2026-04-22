class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.m = 0
            self.n = 0
            return
        
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def _add(self, row, col, delta):
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += delta
                j += j & -j
            i += i & -i

    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._add(row, col, delta)

    def _query(self, row, col):
        s = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                s += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return s

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self._query(row2, col2)
            - self._query(row1 - 1, col2)
            - self._query(row2, col1 - 1)
            + self._query(row1 - 1, col1 - 1)
        )