class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###if len(nums) == 0:
        ###    return 0
        ###i = 0
        ###for j in range(1, len(nums)):
        ###    if nums[i] != nums[j]:
        ###        i += 1
        ###        nums[i] = nums[j]
        ###return i + 1
        
        if not nums:
            return 0
        
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count
