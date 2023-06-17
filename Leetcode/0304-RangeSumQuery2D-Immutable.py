from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            nrow = 0
            ncol = 0
        else:
            nrow = len(matrix)
            ncol = len(matrix[0])
        self.partialsum = [[0] * (ncol + 1) for _ in range(nrow + 1)]

        for i in range(nrow):
            for j in range(ncol):
                self.partialsum[i + 1][j + 1] = (
                    self.partialsum[i][j + 1]
                    + self.partial[i + 1][j]
                    - self.partial[i][j]
                    + matrix[i][j]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self.partialsum[row2 + 1][col2 + 1]
            - self.partial[row2 + 1][col1]
            - self.partial[row1][col2 + 1]
            + self.partial[row1][col1]
        )


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.parsum = [[0] * (1 + n) for _ in range(1 + m)]

        for i in range(m):
            for j in range(n):
                self.parsum[i + 1][j + 1] = matrix[i][j] + self.parsum[i][j + 1]
        for i in range(m):
            for j in range(n):
                self.parsum[i + 1][j + 1] += self.parsum[i + 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.parsum[row2 + 1][col2 + 1]
            - self.parsum[row2 + 1][col1]
            - self.parsum[row1][col2 + 1]
            + self.parsum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == "__main__":
    res = NumMatrix(
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    )
    param_1 = res.sumRegion(2, 1, 4, 3)
    print(param_1)

    param_1 = res.sumRegion(1, 2, 2, 4)
    print(param_1)
