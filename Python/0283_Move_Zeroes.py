from typing import List


class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) <= 1: return nums
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] != 0:
                l += 1
            while l < r and nums[r] == 0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        nums[:l] = sorted(nums[:l])
        return nums


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         idx = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[idx], nums[i] = nums[i], nums[idx]
#                 idx += 1
#         return nums


if __name__ == "__main__":
    res = Solution().moveZeroes(nums=[0, 1, 0, 3, 12])
    print(res)

    res = Solution().moveZeroes(nums=[0, 0])
    print(res)
