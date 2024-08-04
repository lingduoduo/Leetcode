from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse=True)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        k = k % 2
        if k % 2 == 1:
            nums[-1] = -nums[-1]
        return sum(nums)
