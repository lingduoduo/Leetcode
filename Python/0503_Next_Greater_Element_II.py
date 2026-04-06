from typing import List

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
    # nums = [1,2,1]
    nums = [1, 2, 3, 4, 5]
    # nums = [5, 4, 3, 2, 1]
    results = Solution().nextGreaterElements(nums)
    print(results)
