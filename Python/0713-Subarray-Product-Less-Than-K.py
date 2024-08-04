import numpy as np


class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1:
            return 0

        prod = 1
        res = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
        return res


if __name__ == "__main__":
    nums = [10, 3, 3, 7, 2, 9, 7, 4, 7, 2, 8, 6, 5, 1, 5]
    k = 30
    res = Solution().numSubarrayProductLessThanK(nums, k)
    print(res)
