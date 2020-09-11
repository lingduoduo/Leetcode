class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ###for i in range(len(nums) - 1, -1, -1):
        ###    if nums[i] == 0:
        ###        nums.pop(i)
        ###        nums.append(0)
        
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
        
        for i in range(pos, len(nums)):
            nums[i] = 0
    
        

        
                
                
                