from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0
        for i in range(len(nums)):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1

if __name__ == "__main__":
   res = Solution().removeDuplicates([1, 1, 2])
   print(res)