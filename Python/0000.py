from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        res = 0
        start = 0
        for i, chr in enumerate(s):
            if chr in d:
                d[chr] += 1
            else:
                d[chr] = 1
            while len(d.keys()) > k:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res

if __name__ == "__main__":
    res = Solution().lengthOfLongestSubstringKDistinct(s = "eceba", k = 2)
    print(res)