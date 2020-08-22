class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        left = 0
        right = len(nums)-1
        res = nums[0]
        
        while left <= right:
            mid = left + (right-left)//2
            if nums[left] <= nums[mid]:
                res = min(res, nums[left])
                left = mid + 1
            else:
                res = min(res, nums[mid])
                right = mid -1
        return res
        
        
        
        
