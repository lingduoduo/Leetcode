class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        top, bottom = 0, m - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            col = 0
            for j in range(n):
                if mat[mid][j] > mat[mid][col]:
                    col = j

            up = mat[mid - 1][col] if mid > 0 else -1
            down = mat[mid + 1][col] if mid < m - 1 else -1

            if mat[mid][col] > up and mat[mid][col] > down:
                return [mid, col]
            elif down > mat[mid][col]:
                top = mid + 1
            else:
                bottom = mid - 1