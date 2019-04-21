class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return res

        rowstart = 0
        rowend = len(matrix) - 1
        colstart = 0
        colend = len(matrix[0]) - 1

        while rowstart < rowend and colstart < colend:
            for j in range(colstart, colend):
                res.append(matrix[rowstart][j])
            for i in range(rowstart, rowend):
                res.append(matrix[i][colend])
            for j in range(colend, colstart, -1):
                res.append(matrix[rowend][j])
            for i in range(rowend, rowstart, -1):
                res.append(matrix[i][colstart])
            rowstart += 1
            rowend -= 1
            colstart += 1
            colend -= 1
        if rowstart == rowend and colstart == colend:
            res.append(matrix[rowend][colend])
        elif rowstart == rowend:
            for j in range(colstart, colend + 1):
                res.append(matrix[rowend][j])
        elif colstart == colend:
            for i in range(rowstart, rowend + 1):
                res.append(matrix[i][colend])
        return res

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = Solution().spiralOrder(matrix)
    print(result)
