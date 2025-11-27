from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = res = 0
        d = {}
        for i, num in enumerate(nums):
            presum += num
            if presum == k:
                res = i + 1
            if presum - k in d:
                res = max(res, i - d[presum - k])
            if presum not in d:
                d[presum] = i
        return res
