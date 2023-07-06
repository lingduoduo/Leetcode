from typing import List

class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            while j < len(nums) and nums[i] != 0:
                i += 1
                j += 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
        return nums


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        l = 0
        while l < len(nums):
            if nums[l] != 0:
                l += 1
                continue
            r = l + 1
            while r < len(nums) and nums[r] == 0:
                r += 1
            if r < len(nums) and nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
            l += 1


import pysnooper

@pysnooper.snoop()
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        i = 0
        j = 0
        while j < len(nums):
            while j < len(nums) and nums[i] != 0:
                i += 1
                j += 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1

if __name__ == "__main__":
    # res = Solution().moveZeroes(nums=[0, 1, 0, 3, 12])
    # print(res)

    res = Solution().moveZeroes(nums=[0, 0])
    print(res)