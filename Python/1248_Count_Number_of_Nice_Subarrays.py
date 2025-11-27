import collections
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        d = collections.defaultdict(int)
        d[0] = 1
        presum = 0
        for num in nums:
            if num & 1 == 1:
                presum += 1
            if presum - k in d:
                res += d[presum - k]
            d[presum] += 1
        return res


if __name__ == "__main__":
    res = Solution().numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2)
    print(res)
