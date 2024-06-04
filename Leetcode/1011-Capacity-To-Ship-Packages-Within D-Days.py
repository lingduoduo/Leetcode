from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(cap):
            day_need, cur_load = 1, 0
            for weight in weights:
                cur_load += weight
                if cur_load > cap:
                    cur_load = weight
                    day_need += 1
                    if day_need > days:
                        return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            if helper(m):
                r = m
            else:
                l = m + 1
        return l