from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:        
        m, n = len(nums1), len(nums2)

        # dp[i][j] = max dot product of subsequences
        dp = [[float("-inf")] * (n + 1) for _ in range(m + 1)]

        # fill from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prod = nums1[i] * nums2[j]
                dp[i][j] = max(
                    prod,                   # take (i, j) and end
                    prod + dp[i + 1][j + 1], # take (i, j) and continue
                    dp[i + 1][j],            # skip nums1[i]
                    dp[i][j + 1],            # skip nums2[j]
                )

        return dp[0][0]
    
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        # dp[i][j] = max dot product of subsequences
        dp = [[float("-inf")] * (n + 1) for _ in range(m + 1)]

        m, n = len(nums1), len(nums2)
        dp = [[float("-inf")] * n for _ in range(m)]

        # fill from top-left to bottom-right
        for i in range(m):
            for j in range(n):
                prod = nums1[i] * nums2[j]

                dp[i][j] = max(
                    prod,  # start new subsequence
                    prod + (max(dp[i - 1][j - 1], 0) if i and j else 0),  # extend
                    dp[i - 1][j] if i else float("-inf"),  # skip nums1[i]
                    dp[i][j - 1] if j else float("-inf"),  # skip nums2[j]
                )

        return dp[-1][-1]
   