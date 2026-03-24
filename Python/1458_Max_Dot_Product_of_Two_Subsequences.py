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
        neg_inf = float("-inf")
        
        # dp[i][j] = max dot product using nums1[:i], nums2[:j]
        dp = [[neg_inf] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prod = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(
                    prod,                           # start new subsequence here
                    prod + max(dp[i - 1][j - 1], 0),  # extend previous subsequence
                    dp[i - 1][j],                  # skip nums1[i - 1]
                    dp[i][j - 1],                  # skip nums2[j - 1]
                )

        return dp[-1][-1]

   