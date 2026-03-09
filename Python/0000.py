from typing import List
import heapq
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        res = 0

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= start:
                start = d[ch] + 1
            d[ch] = i
            res = max(res, i - start + 1)

        return res
            
                


                


if __name__ == "__main__":
    res = Solution().medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    print(res)
