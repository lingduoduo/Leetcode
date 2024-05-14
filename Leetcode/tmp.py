from typing import List, Optional
import heapq

import collections

class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left = sum([1 for c in s[:i] if c == '0'])
            right = sum([1 for c in s[i:] if c == '1'])
            res = max(res, left + right)
        return res


# Test the code        
if __name__ == '__main__':
    res = Solution().maxScore("011101")
    print(res)