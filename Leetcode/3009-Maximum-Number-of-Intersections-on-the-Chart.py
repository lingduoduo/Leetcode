from collections import defaultdict
from typing import List
class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        d = defaultdict(int)
        for i, (left, right) in enumerate(zip(y, y[1:])):
            print(d)
            if i == 0:
                start = min(left, right)
                end = max(left, right)
                end += 0.5
            else:
                if left > right:
                    start = right
                    end = left
                else:
                    start = left + 0.5
                    end = right + 0.5

            d[start] += 1
            d[end] -= 1
        preSum = 0
        res = 0
        for key in sorted(d.keys()):
            preSum += d[key]
            res = max(res, preSum)
        return res

if __name__ == "__main__":
    res = Solution().maxIntersectionCount(y = [1,2,1,2,1,3,2])
    print(res)