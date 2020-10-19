class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        dp = [0] * (s + 1)
        dp[0] = 1
        for num in nums:
            for i in range(s, -1, -1):
                if dp[i]:
                    dp[i+num] = 1
                    
            if dp[s//2]:
                return True
            
        return False