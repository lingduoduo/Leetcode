from typing import List


class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0

        if nums == [val]:
            return 0

        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] != val:
                left += 1
            else:
                while left < right and nums[right] == val:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
        return [num != val for num in nums].count(True)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    # nums = [3, 4, 5]
    results = Solution().removeElement(nums, 3)
    print(results)
