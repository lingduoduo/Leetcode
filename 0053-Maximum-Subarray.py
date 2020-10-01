# class Solution(object):
#     def maxSubArray(self, nums):
        ###f = [0] * len(nums)
        ###f[0] = nums[0]
        ###for i in range(1, len(nums)):
        ###    f[i] = max(f[i - 1] + nums[i], nums[i])
        ###return max(f)
        
        # if max(nums)<0:
        #     return max(nums)
        
        # local_max, global_max = 0, 0
        # for num in nums:
        #     local_max = max(0, local_max + num)
        #     print(local_max)
        #     global_max = max(global_max, local_max)
        # return global_max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        
        dp = [0]*(len(nums))
        dp[0] = max(dp[0], nums[0])
        
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]+nums[i])
        print(dp)
        return max(dp)
                
if __name__ == "__main__":
    # numbers = [-2,1,-3,4,-1,2,1,-5,4]
    numbers = [-2,1]
    result = Solution().maxSubArray(numbers)
    print(result)
