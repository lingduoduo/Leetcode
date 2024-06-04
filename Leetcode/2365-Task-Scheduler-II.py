from typing import List
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        res = 0
        d = {}
        for task in tasks:
            res += 1
            if task in d:
                res = max(res, d[task] + space + 1)
            d[task] = res
        return res
