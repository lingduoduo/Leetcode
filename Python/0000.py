from typing import List
import heapq
from collections import defaultdict
import random

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            d = defaultdict(int)
            distinct = 0
            max_freq = 0

            for j in range(i, n):
                d[s[j]] += 1

                if d[s[j]] == 1:
                    distinct += 1
                max_freq = max(max_freq, d[s[j]])

                if (j - i + 1) == distinct * max_freq:
                    res = max(res, j - i + 1)

        return res
        


if __name__ == "__main__":
    res = Solution().longestBalanced(s = "abbac")
    print(res)
