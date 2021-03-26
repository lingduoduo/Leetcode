class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = nums[0]
        local = prev
        res = local
        
        for i in range(1,  len(nums)):
            if nums[i] > prev:
                local += nums[i]
                prev = nums[i]
            else:
                res = max(res, local)
                prev = nums[i]
                local = prev
        res = max(res, local)
        return res
        