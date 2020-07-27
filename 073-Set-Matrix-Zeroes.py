class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows = set()
        # cols = set()
        #
        # n = len(matrix)
        # m = len(matrix[0])
        #
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        # for row in rows:
        #     for j in range(m):
        #         matrix[row][j] = 0
        #
        # for col in cols:
        #     for i in range(n):
        #         matrix[i][col] = 0
        # return matrix


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
