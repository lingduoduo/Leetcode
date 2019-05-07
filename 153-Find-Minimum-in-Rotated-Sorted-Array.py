class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        
        while start < end:
            if nums[start] < nums[mid]:
                start = mid + 1
            if nums[end] < nums[mid]:
