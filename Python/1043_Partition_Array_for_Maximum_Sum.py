from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (1 + n)
        for start in range(n - 1, -1, -1):
            currMax = 0
            end = min(n, start + k)
            for i in range(start, end):
                currMax = max(currMax, arr[i])
                # Store the maximum of all options for the current subarray.
                dp[start] = max(dp[start], dp[i + 1] + currMax * (i - start + 1))
        return dp[0]
