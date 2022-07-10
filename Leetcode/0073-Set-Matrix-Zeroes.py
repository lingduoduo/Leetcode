class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for j in range(m):
                matrix[row][j] = 0

        for col in cols:
            for i in range(n):
                matrix[i][col] = 0
        return matrix


class Solution:
    def setZeroes(self, matrix) -> None:
        nrow = len(matrix)
        ncol = len(matrix[0])
        zero_row, zero_col = False, False

        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    zero_row = True if i == 0 else zero_row
                    zero_col = True if j == 0 else zero_col

        for j in range(1, ncol):
            if matrix[0][j] == 0:
                for i in range(1, nrow):
                    matrix[i][j] = 0

        for i in range(1, nrow):
            if matrix[i][0] == 0:
                for j in range(1, ncol):
                    matrix[i][j] = 0

        if zero_row:
            for j in range(ncol):
                matrix[0][j] = 0

        if zero_col:
            for i in range(nrow):
                matrix[i][0] = 0

        return matrix


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [
        [1, 0, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]
    result = Solution().setZeroes(matrix)
    print(result)

    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    result = Solution().setZeroes(matrix)
    print(result)
