from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        d = {}
        for i in range(length + 1):
            d[i] = 0

        for start, end, val in updates:
            d[start] += val
            d[end + 1] -= val

        presum = 0
        res = []
        for v in d.values():
            res.append(presum + v)
            presum += v
        return res[:-1]
