class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        nrow = len(matrix)

        for i in range(nrow):
            for j in range(nrow - i):
                matrix[i][j], matrix[nrow - 1 - j][nrow - 1 -
                                                   i] = matrix[nrow - 1 - j][nrow - 1 - i], matrix[i][j]

        for i in range(nrow // 2):
            for j in range(nrow):
                matrix[i][j], matrix[nrow - 1 - \
                    i][j] = matrix[nrow - 1 - i][j], matrix[i][j]

        return matrix


if __name__ == '__main__':
    input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = Solution().rotate(input)
    print(result)
