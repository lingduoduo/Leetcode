class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## First try
        if target < nums[0]:
        	return 0

        for i in range(len(nums)):
        	if target <= nums[i]:
        		return i
        return len(nums)

        ## Second try
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=left+(right-left)/2
            
            if nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            elif nums[mid]==target:
                return mid

            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1

        return left
