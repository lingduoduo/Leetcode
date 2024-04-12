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
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return nums


if __name__ == "__main__":
    res = Solution().moveZeroes(nums=[0, 1, 0, 3, 12])
    print(res)

    res = Solution().moveZeroes(nums=[0, 0])
    print(res)
