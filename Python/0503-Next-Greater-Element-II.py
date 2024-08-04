from typing import List


class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        padding = nums * 2
        res = [-1] * len(padding)

        for i in reversed(range(len(padding))):
            if stack and padding[i] < stack[-1]:
                res[i] = stack[-1]
            elif stack and padding[i] >= stack[-1]:
                while stack and padding[i] >= stack[-1]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
            stack.append(padding[i])
        return [res[len(nums)]] + res[1 : len(nums)]


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [0]
        n = len(nums)
        nums = nums + nums
        for i in range(1, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                prev = stack.pop()
                res[prev % n] = nums[i]
            stack.append(i)
        return res


if __name__ == "__main__":
    # nums = [1,2,1]
    nums = [1, 2, 3, 4, 5]
    # nums = [5, 4, 3, 2, 1]
    results = Solution().nextGreaterElements(nums)
    print(results)
