class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        n = len(nums)
        
        dp_max = [0] * n
        dp_min = [0] * n
        
        dp_max[0] = dp_min[0] = res = nums[0]
        
        for i in range(1, n):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            res = max(res, dp_max[i])
            
        return res

