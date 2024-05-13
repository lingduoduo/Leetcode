import collections
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        directions = [(-1, 1), (1, -1)]

        count = 0

        res = []

        i, j = 0, 0

        m, n = len(matrix), len(matrix[0])

        while len(res) < m * n:
            if 0 <= i < m and 0 <= j < n:
                res.append(matrix[i][j])
                direct = directions[count % 2]
                i, j = i + direct[0], j + direct[1]
                continue
            elif i < 0 and 0 <= j < n:
                i += 1
            elif i < m and j < 0:
                j += 1
            elif i < m and j >= n:
                i += 2
                j -= 1
            elif i >= m and j < n:
                j += 2
                i -= 1
            count += 1
        return res


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        n, m = len(matrix), len(matrix[0])
        row, col = 0, 0
        direction = 1
        res = []
        while row < n and col < m:
            res.append(matrix[row][col])
            new_row = row + (-1 if direction == 1 else 1)
            new_column = col + (1 if direction == 1 else -1)
            if new_row < 0 or new_row == n or new_column < 0 or new_column == m:
                if direction:
                    row += column == m - 1
                    column += column < m - 1
                else:
                    column += row == n - 1
                    row += row < n - 1
                dir = 1 - dir
            else:
                row = new_row
                column = new_column
        return res

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d= collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i+j].append(mat[i][j])
        res = []
        for entry in d.items():
            if entry[0] % 2 == 0:
                res.extend(entry[1][::-1])
            else:
                res.extend(entry[1])
        return res
