class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        for x in range(1, size - 1):
            if nums[x] > nums[x - 1] and nums[x] > nums[x + 1]:
                return x
        return [0, size - 1][nums[0] < nums[size - 1]]
    