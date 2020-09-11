class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ###if not nums:
        ###    return 0
        ###if len(nums) == 1:
        ###    return nums[0]
        #
        ###dp = [0] * (len(nums) + 1)
        ###dp[0] = 0
        ###dp[1] = nums[0]
        ###for i in range(1, len(nums)):
        ###    dp[1 + i] = max(dp[i - 1] + nums[i], dp[i])
        #
        ###return dp[len(nums)]
        
        last, now  = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
            
        return now
