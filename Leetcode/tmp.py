from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all([(x - y) <= 0 for x, y in zip(nums, nums[1:])]) or all([(x - y) >= 0 for x, y in zip(nums, nums[1:])])

if __name__ == "__main__":
    res = Solution().isMonotonic(nums = [1,2,2,3])
    print(res)
