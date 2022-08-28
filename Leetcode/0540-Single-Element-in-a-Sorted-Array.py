from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = set(nums)
        return 2 * sum(s) - sum(nums)


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1:]:
            res ^= num
        return res


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            print(m)
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                h = m
        return nums[l]


if __name__ == "__main__":
    res = Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(res)
