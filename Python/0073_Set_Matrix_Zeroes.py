from typing import List

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
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(m))
        first_col_zero = any(matrix[i][0] == 0 for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 0]]
    result = Solution().setZeroes(matrix)
    print(result)

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    result = Solution().setZeroes(matrix)
    print(result)
