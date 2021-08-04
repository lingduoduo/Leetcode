class Solution:
    def printMatrix(self, matrix):
        r1 = 0
        r2 = len(matrix) - 1
        c1 = 0
        c2 = len(matrix[0]) - 1

        res = []
        while r1 <= r2 and c1 <= c2:
            for j in range(c1, c2 + 1 ):
                res.append(matrix[r1][j])
            r1 += 1

            for i in range(r1, r2 + 1):
                res.append(matrix[i][c2])
            c2 -= 1

            for j in reversed(range(c1, c2 + 1)):
                res.append(matrix[r2][j])
            r2 -= 1
            

            for i in reversed(range(r1, r2 + 1)):
                res.append(matrix[i][c1])
            c1 += 1
        return res          

if __name__ == '__main__':
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    res = Solution().printMatrix(matrix)
    print(res)
