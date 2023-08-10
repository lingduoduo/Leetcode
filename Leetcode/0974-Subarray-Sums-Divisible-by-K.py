from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presum = 0
        res = 0
        d = collections.Counter()
        d[0] = 1
        for num in nums:
            presum += num
            res += d[presum % k]
            d[presum % k] += 1
        return res
