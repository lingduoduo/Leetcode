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
            elif i >= m and j < n :
                j += 2
                i -= 1
            count += 1
        return res
