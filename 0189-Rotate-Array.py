class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ###changed = list()
        ###while k > len(nums):
        ###    k -= len(nums)
        ###changed = nums[-k:] + nums[:-k]
        ###for i in range(len(nums)):
        ###    nums[i] = changed[i]
        k = k % len(nums)
        
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
       
