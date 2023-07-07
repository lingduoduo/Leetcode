from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left, right = 0, 0
        csum = 0
        res = float("inf")
        while right < len(nums):
            csum += nums[right]
            while target <= csum:
                res = min(res, right - left + 1)
                csum -= nums[left]
                left += 1
            right += 1
        return res

        #


# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if sum(nums) < target:
#             return 0
#
#         stack = []
#         psum = 0
#         res = len(nums)
#         for num in nums:
#             psum += num
#             stack.append(num)
#             while stack and psum >= target:
#                 res = min(res, len(stack))
#                 val = stack.pop(0)
#                 psum -= val
#         return res


if __name__ == "__main__":
    # s=15
    # nums = [1,2,3,4,5]
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = Solution().minSubArrayLen(s, nums)
    print(result)
