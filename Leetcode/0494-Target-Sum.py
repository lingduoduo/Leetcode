from typing import List
from typing import collections


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(1 + n)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for k, v in dp[i].items():
                dp[i + 1][k - num] += v
                dp[i + 1][k + num] += v
        return dp[n][target]


if __name__ == "__main__":
    res = Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3)
    print(res)
