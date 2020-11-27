import numpy as np
class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1: return 0
        n = len(nums)
        res = 0
        for i in range(n):
            tmp = 1
            for j in range(i+1, n):
                tmp *= nums[j]
                if  tmp < k:
                    print([i,j])
                    res += 1
                    continue
        return res

if __name__ == '__main__':
    nums = [10,3,3,7,2,9,7,4,7,2,8,6,5,1,5]
    k = 30
    res = Solution().numSubarrayProductLessThanK(nums, k)
    print(res)
