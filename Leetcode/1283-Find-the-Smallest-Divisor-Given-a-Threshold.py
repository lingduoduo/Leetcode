from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums) + 1
        res = 0
        while left < right:
            mid = left + (right - left) // 2
            tot = sum((x - 1) // mid + 1 for x in nums)
            if tot <= threshold:
                res = mid
                right = mid
            else:
                left = mid + 1
        return res


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums) + 1

        res = 0
        while left < right:
            mid = left + (right - left) // 2
            cur = 0
            for i in range(len(nums)):
                cur += math.ceil(nums[i] / mid)
            if cur <= threshold:
                res = mid
                right = mid
            else:
                left = mid + 1
        return res
