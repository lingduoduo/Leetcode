from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        stack = []
        for i, num in enumerate(nums):
            cur = 0
            while stack and nums[stack[-1]] <= num:
                cur = max(cur, dp[stack.pop()])
            if stack:
                dp[i] = cur + 1
            stack.append(i)
        return max(dp)
