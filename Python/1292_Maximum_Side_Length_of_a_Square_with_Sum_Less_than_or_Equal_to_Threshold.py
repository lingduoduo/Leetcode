from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        if m == 0:
            return 0
        n = len(mat[0])

        # build 2D prefix-sum
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = (
                    presum[i - 1][j]
                    + presum[i][j - 1]
                    - presum[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        left, right = 0, min(m, n) + 1  # search in [0, min(m,n)]
        res = 0
        while left < right:
            mid = left + (right - left) // 2
            valid = False
            if mid > 0:
                for i in range(mid, m + 1):
                    for j in range(mid, n + 1):
                        cursum = (
                            presum[i][j]
                            - presum[i - mid][j]
                            - presum[i][j - mid]
                            + presum[i - mid][j - mid]
                        )
                        if cursum <= threshold:
                            valid = True
                            break
                    if valid:
                        break

            if valid:
                res = mid
                left = mid + 1
            else:
                right = mid

        return res

