from collections import defaultdict
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        res = [-1] * len(nums)
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] < v:
                p = stack.pop()
                res[p] = v
            stack.append(i)
        return res[:n]
                
if __name__ == "__main__":
    res = Solution().nextGreaterElements(nums = [1,2,3,4,3])
    print(res)
