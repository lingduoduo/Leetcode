import collections
from typing import List
from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        d_left = defaultdict(int)
        d_right = collections.Counter(s)

        res = 0
        left = 0
        right = len(d_right)

        for chr in s:
            if d_left[chr] == 0:
                left += 1
            d_left[chr] += 1

            d_right[chr] -= 1
            if d_right[chr] == 0:
                right -= 1

            if left == right:
                res += 1

        return res

if __name__ == '__main__':
    res = Solution().numSplits(s = "abcd")
    print(res)
