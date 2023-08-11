from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        tot = sum(nums)
        res = []
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            left = math.floor(cur / (i + 1))
            right = math.floor((tot - cur) / max(1, (len(nums) - i - 1)))
            res.append(abs(left - right))
        return res.index(min(res))
