# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#
#         res = []
#         if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
#             return res
#
#         rowstart = 0
#         rowend = len(matrix) - 1
#         colstart = 0
#         colend = len(matrix[0]) - 1
#
#         while rowstart < rowend and colstart < colend:
#             for j in range(colstart, colend):
#                 res.append(matrix[rowstart][j])
#             for i in range(rowstart, rowend):
#                 res.append(matrix[i][colend])
#             for j in range(colend, colstart, -1):
#                 res.append(matrix[rowend][j])
#             for i in range(rowend, rowstart, -1):
#                 res.append(matrix[i][colstart])
#             rowstart += 1
#             rowend -= 1
#             colstart += 1
#             colend -= 1
#
#         if rowstart == rowend and colstart == colend:
#             res.append(matrix[rowend][colend])
#         elif rowstart == rowend:
#             for j in range(colstart, colend + 1):
#                 res.append(matrix[rowend][j])
#         elif colstart == colend:
#             for i in range(rowstart, rowend + 1):
#                 res.append(matrix[i][colend])
#         return res
#
#
# class Solution(object):
#     def spiralOrder(self, matrix):
#         row = len(matrix)
#         if row == 0:
#             return []
#         col = len(matrix[0])
#         if col ==0:
#             return []
#
#         res = matrix[0] ###1,2,3
#         if row>1:
#             for i in range(1, row):
#                 res.append(matrix[i][col-1]) ###3,6,9
#             for j in range(col-2, -1, -1):
#                 res.append(matrix[row-1][j]) ###9,8,7
#             if col>1:
#                 for i in range(row-2, 0, -1):
#                     res.append(matrix[i][0]) ###7,4,1
#         M = []
#         for k in range(1, row-1):
#             t = matrix[k][1:-1]
#             M.append(t)
#         return res + self.spiralOrder(M)


class Solution:
    def spiralOrder(self, matrix):
        ret = []
        r1 = 0
        r2 = len(matrix) - 1
        c1 = 0
        c2 = len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                ret.append(matrix[r1][i])
            for i in range(r1 + 1, r2 + 1):
                ret.append(matrix[i][c2])
            if r1 != r2:
                for i in reversed(range(c1, c2)):
                    ret.append(matrix[r2][i])
            if c1 != c2:
                for i in reversed(range(r1 + 1, r2)):
                    ret.append(matrix[i][c1])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return ret


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = Solution().spiralOrder(matrix)
    print(result)

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = Solution().spiralOrder(matrix)
    print(result)
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
