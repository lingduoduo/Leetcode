from typing import List
import collections

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        d = collections.Counter()
        start = 0
        res = 0

        for i, v in enumerate(nums):
            d[v] += 1

            while len(d) > k:
                d[nums[start]] -= 1
                if d[nums[start]] == 0:
                    del d[nums[start]]
                start += 1
            res += i - start + 1

        return res
