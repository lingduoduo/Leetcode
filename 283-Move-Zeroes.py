class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = list()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                pos.append(i)
        for i in pos:
            nums.pop(i)
            nums.append(0)