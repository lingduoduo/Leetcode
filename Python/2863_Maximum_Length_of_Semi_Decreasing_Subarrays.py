from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        res = 0
        cur = float('-inf')
        for i in range(n):
            while stack and stack[-1] <= i:
                stack.pop()
            if nums[i] > cur:
                cur = nums[i]
                while stack and nums[stack[-1]] < cur:
                    res = max(res, stack[-1] - i + 1)
                    stack.pop()
        
        return res