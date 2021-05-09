class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = 0
        res = float('-inf')
        
        
        for idx, num in enumerate(nums):
            tmp += num
            if idx>=k:
                tmp -= nums[idx-k]
            if idx>=k-1:
                res = max(res, tmp)
        res = res/k
        
        return res
        
        