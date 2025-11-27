from typing import List
import math


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        presum = res = nums[0]
        for i in range(1, len(nums)):
            presum += nums[i]
            res = max(res, math.ceil(presum / (i + 1)))
        return res
