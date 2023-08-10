from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        res = 0
        cumsum = 0
        for i, num in enumerate(nums):
            if num == 0:
                cumsum -= 1
            else:
                cumsum += 1

            if cumsum in d:
                res = max(res, i - d[cumsum])
            else:
                d[cumsum] = i

        return res


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        res = 0
        presum = 0
        for i, num in enumerate(nums):
            presum += 1 if num == 1 else -1
            if presum in d:
                res = max(res, i - d[presum])
            else:
                d[presum] = i
        return res
