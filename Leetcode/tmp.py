import collections
from typing import List
from collections import defaultdict

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        d = collections.defaultdict(int)
        parsum = 0
        res = 0
        for i, h in enumerate(hours):
            if h > 8:
                parsum += 1
            else:
                parsum -= 1
            if parsum > 0:
                res = i + 1
            if parsum not in d:
                d[parsum] = i
            if parsum - 1 in d:
                res = max(res, i - d[parsum -1])
        return res


if __name__ == "__main__":
    res = Solution().productExceptSelf(nums = [-1,1,0,-3,3])
    print(res)  

