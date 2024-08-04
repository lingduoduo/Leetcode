from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        for i in range(N - 2):
            if nums[N - 1 - i] < nums[N - 1 - i - 1] + nums[N - 1 - i - 2]:
                return nums[N - 1 - i] + nums[N - 1 - i - 1] + nums[N - 1 - i - 2]
        return 0
