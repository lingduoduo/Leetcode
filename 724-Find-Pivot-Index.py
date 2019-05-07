class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        dp = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            dp[i + 1] = dp[i] + nums[i]
        
        result = -1
        for i in range(len(nums)):
            if dp[i] == dp[-1] - dp[i + 1]:
                result = i
        
        return result
    
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        N = len(nums)
        sums = [0] * (N + 1)
        for i in range(N):
            sums[i + 1] = sums[i] + nums[i]
        for i in range(N):
            if sums[i] == sums[-1] - sums[i + 1]:
                return i
        return -1
