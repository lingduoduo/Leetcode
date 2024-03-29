from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 0
        curr = 0
        for i in range(1, len(nums)):
            if nums[curr] != nums[i]:
                times = 0
                curr += 1
                nums[curr] = nums[i]
            elif nums[curr] == nums[i] and times == 0:
                times += 1
                curr += 1
                nums[curr] = nums[i]

        return nums[:curr]


class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[idx]:
                cnt += 1
                if cnt == 2:
                    idx += 1
                    nums[idx] = nums[i]
            else:
                cnt = 1
                idx += 1
                nums[idx] = nums[i]
        return idx + 1


if __name__ == "__main__":
    numbers = [1, 1, 1, 2, 2, 3]
    # numbers = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    result = Solution().removeDuplicates(numbers)
    print(result)
