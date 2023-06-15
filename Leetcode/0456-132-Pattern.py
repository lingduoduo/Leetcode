import itertools


class Solution(object):
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        res = itertools.combinations(nums, 3)
        for i in res:
            if i[0] < i[2] < i[1]:
                return True
        return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second_min = float("-inf")
        for i in reversed(range(len(nums))):
            if nums[i] < second_min:
                return True
            while stack and nums[i] > stack[-1]:
                second_min = stack.pop()
            stack.append(nums[i])
        return False
