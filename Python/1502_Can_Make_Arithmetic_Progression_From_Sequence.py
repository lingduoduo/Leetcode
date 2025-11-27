class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        nums = sorted(arr)
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] != diff:
                return False
        return True
