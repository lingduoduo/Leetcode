class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for idx, num in enumerate(nums):
            while stack and stack[-1] > num and k - len(stack) < len(nums) - idx:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
