from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 0, sum(batteries)
        res = 0
        while l <= r:
            m = l + (r - l)//2
            reserve = 0

            for v in batteries:
                reserve += min(v, m)
            
            if reserve >= m * n:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res






