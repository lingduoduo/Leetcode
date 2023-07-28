from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if a == b:
                    if i >= 1 and j >= 1:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                    else:
                        dp[i][j] = 1
        return dp[-1][-1]


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
