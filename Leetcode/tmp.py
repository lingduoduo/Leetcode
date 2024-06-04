from  collections import Counter
from typing import List
import collections


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


if __name__ == "__main__":
    res = Solution().taskSchedulerII(tasks = [5,8,8,5], space = 2)
    print(res)



