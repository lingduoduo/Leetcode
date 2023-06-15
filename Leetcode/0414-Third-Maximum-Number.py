class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###nums = list(set(nums))
        #
        ###max_1 = max_2 = max_3 = float('-inf')
        #
        ###for i in range(len(nums)):
        ###    if nums[i]>max_1:
        ###        max_3 = max_2
        ###        max_2 = max_1
        ###        max_1 = nums[i]
        ###    elif nums[i]>max_2:
        ###        max_3 = max_2
        ###        max_2 = nums[i]
        ###    elif nums[i]>max_3:
        ###        max_3 = nums[i]
        ###return max_1 if max_3 == float('-inf') else max_3

        nums = sorted(list(set(nums)))

        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]
