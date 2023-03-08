class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        nums.sort()

        res = float("-inf")

        for i in range(1, len(nums)):
            res = max(res, abs(nums[i] - nums[i - 1]))

        return res
