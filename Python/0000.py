from typing import List
from collections import Counter
import heapq
import re
from collections import deque

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # 1. Feasibility check: every char in target must be in source
        if not set(target).issubset(set(source)):
            return -1

        i = 0
        j = 0
        n = len(source)

        while True:
            # Try to match as many chars as possible in this "run"
            while j < len(target) and source[i % n] == target[j]:
                i += 1
                j += 1

            # If we’ve matched the whole target, compute how many subsequences we used
            if j == len(target):
                # i characters of source have been consumed in a cyclic way
                # number of full passes over source = ceil(i / n)
                return i // n + (1 if i % n else 0)

            # Otherwise, skip this mismatching character in the cyclic source
            if source[i % n] != target[j]:
                i += 1
        
if __name__ == "__main__":
    res = Solution().shortestWay(source = "aaaaa", target = "aaaaaaaaaaaaa")
    print(res)
