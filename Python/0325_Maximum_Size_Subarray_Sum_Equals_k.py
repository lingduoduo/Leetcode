from typing import List
    
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = 0
        res = 0
        d = {0: -1}

        for i, num in enumerate(nums):
            presum += num

            if presum - k in d:
                res = max(res, i - d[presum - k])

            if presum not in d:
                d[presum] = i
        return res