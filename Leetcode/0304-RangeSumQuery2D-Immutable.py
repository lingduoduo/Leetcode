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
