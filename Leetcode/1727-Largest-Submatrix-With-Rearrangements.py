from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for j in range(n):
            for i in range(1, m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        res = 0
        for i in range(m):
            tmp = sorted(matrix[i][:], reverse=True)
            print(tmp)
            for j in range(n):
                res = max(res, (j + 1) * tmp[j])
        return res



if __name__ == '__main__':
    matrix = [[0,0,1],[1,1,1],[1,0,1]]
    res = Solution().largestSubmatrix(matrix)
    print(res)