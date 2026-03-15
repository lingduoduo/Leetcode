from typing import List
import heapq
from collections import defaultdict
import random

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        n = len(s)
        d = {v: i for i, v in enumerate(list(order))}
        return sorted(s, key=lambda x: d.get(x, n+1))

if __name__ == "__main__":
    res = Solution().customSortString(order = "cba", s = "abcd")
    print(res)
