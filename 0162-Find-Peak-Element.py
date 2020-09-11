class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ###size = len(nums)
        ###for x in range(1, size - 1):
        ###    if nums[x] > nums[x - 1] and nums[x] > nums[x + 1]:
        ###        return x
        ###return [0, size - 1][nums[0] < nums[size - 1]]
        left, right = 0, len(nums) - 1
        while left<=right:
            mid1 = left + (right-left)//2
            mid2 = mid1 + 1

            if nums[mid1]<nums[mid2]:
                left = mid2
            else:
                right = mid1

        if nums[left]<nums[right]:
            return right
        else:
            return left