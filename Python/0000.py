from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect 

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0

        for ch in s:
            if ch == "(":
                l += 1
            else:
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return l + r

            
if __name__ == "__main__":
    print(Solution().minAddToMakeValid(s = "((("))
