class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])

        for i in range(ncol):
            tmp  = []
            x = 0
            y = i 
            while 0 <= x < nrow and 0 <= y < ncol:
                tmp.append(matrix[x][y])
                x += 1
                y += 1
            if len(set(tmp)) > 1:
                return False

        for i in range(1, nrow):
            tmp  = []
            x = i
            y = 0
            while 0 <= x < nrow and 0 <= y < ncol:
                tmp.append(matrix[x][y])
                x += 1
                y += 1
            if len(set(tmp)) > 1:
                return False
        return True

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    res = Solution().isToeplitzMatrix(matrix)
    print(res)