class Solution:
    def find(self, target: int, matrix):
        n = len(matrix)
        m = len(matrix[0])

        if not matrix or n == 0 or m == 0:
            return False

        r = 0
        c = m - 1
        while r < n and c < m:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False

if __name__ == '__main__':
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]]
    res = Solution().find(5, matrix)
    print(res)

    res = Solution().find(100, matrix)
    print(res)