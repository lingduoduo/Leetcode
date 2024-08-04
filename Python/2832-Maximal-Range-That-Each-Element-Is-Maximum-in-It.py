from typing import List


class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        stack = [0]
        nums.append(float("inf"))
        for i in range(1, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                left = -1 if not stack else stack[-1]
                res[idx] = i - left - 1
            stack.append(i)
        return res
