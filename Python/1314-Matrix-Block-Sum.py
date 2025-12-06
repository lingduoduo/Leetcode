from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m , n = len(mat), len(mat[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + mat[i - 1][ j - 1]
        
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)
                res[i][j] = (
                    presum[r2 + 1][c2 + 1]
                    - presum[r1][c2 + 1]
                    - presum[r2 + 1][c1]
                    + presum[r1][c1]
                )
        return res


if __name__ == "__main__":
    res = Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
    print(res)