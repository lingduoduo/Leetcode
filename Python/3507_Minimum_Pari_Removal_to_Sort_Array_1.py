from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(a: List[int]) -> bool:
            return all(a[i] <= a[i + 1] for i in range(len(a) - 1))
        res = 0
        while not is_sorted(nums):
            # find index i that minimizes nums[i] + nums[i+1]
            best_i = 0
            best_sum = nums[0] + nums[1]
            for i in range(1, len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < best_sum:
                    best_sum = s
                    best_i = i

            # merge that pair
            nums[best_i] = best_sum
            nums.pop(best_i + 1)
            res += 1

        return res
