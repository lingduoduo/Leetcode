class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # nrow = len(matrix)
        
        # for i in range(nrow):
        #     for j in range(nrow - i):
        #         matrix[i][j], matrix[nrow-1-j][nrow-1-i] = matrix[nrow- 1 - j][nrow - 1 - i], matrix[i][j]
        
        # for i in range(nrow // 2):
        #     for j in range(nrow):
        #         matrix[i][j], matrix[nrow - 1 - i][j] = matrix[nrow - 1 - i][j], matrix[i][j]
        
        # return matrix

        h = len(matrix)
        n = h - 1

        for i in range(h//2):
            for j in range(i, n-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = tmp





# if __name__ == '__main__':
#     input = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     for col in zip(*input):
#         print(col[::-1])

    # result = Solution().rotate(input)
    # print(result)
