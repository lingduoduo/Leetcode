from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res = 0
        left = 0
        for right in range(len(nums)):
            if right > 0 and nums[right] == nums[right - 1]:
                left = right

            res += right - left + 1
        return res