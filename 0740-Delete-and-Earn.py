from typing import List
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        r = [0 for i in range(max(nums)+1)]

        for idx, num in enumerate(nums):
            r[num] += num
            
        r.pop(0)
        return self.rob(r)
    
    def rob(self, nums):
        dp1, dp2 = 0, 0
        for i in range(len(nums)):
            dp = max(dp1, dp2+nums[i])
            dp2 = dp1
            dp1 = dp
        return dp

if __name__ == '__main__':
    # nums = [2, 2, 3, 3, 3, 4]
    nums = [3, 4,  2]
    res = Solution().deleteAndEarn(nums)
    print(res)

