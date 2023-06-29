from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (1 + len(B)) for _ in range(1 + len(A))]

        res = 0
        for i in range(1, 1 + len(A)):
            for j in range(1, 1 + len(B)):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res
