class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []

        for col in zip(*matrix):
            res.append(col[::-1])

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = res[i][j]  #


class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = reversed(matrix[i])


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    results = Solution().rotate(input)
