class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)

        dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        return max(dp)
