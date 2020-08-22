class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # nums = sorted(nums, reverse=True)
        # return max(nums[0]*num[1]*nums[2], nums[0]*nums[n-2]*nums[n-1])
        
        n = len(nums)
        MAX_1 = MAX_2 = MAX_3 = -1000
        MIN_1 = MIN_2 = 1000
        for i in range(n):
            if nums[i] > MAX_1:
                MAX_3 = MAX_2
                MAX_2 = MAX_1
                MAX_1 = nums[i]
            elif nums[i] > MAX_2:
                MAX_3 = MAX_2
                MAX_2 = nums[i]
            elif nums[i] > MAX_3:
                MAX_3 = nums[i]
            
            if nums[i] < MIN_1:
                MIN_2 = MIN_1
                MIN_1 = nums[i]
            elif nums[i] < MIN_2:
                MIN_2 = nums[i]
        return max(MAX_1 * MAX_2 * MAX_3, MAX_1 * MIN_1 * MIN_2)
