from typing import List
import heapq
from collections import defaultdict
import random

class Solution:
    def __init__(self, w: List[int]):
        self.presum = [w[0]]
        for v in w[1:]:
            self.presum.append(self.presum[-1] + v)
        self.total = self.presum[-1]

    def pickIndex(self) -> int:
        target = random.random() * self.total
        l, r = 0, len(self.presum)
        
        while l < r:
            m = l + (r - l)//2
            if self.presum[m] < target:
                l = m + 1
            else:
                r = m
        return l 

if __name__ == "__main__":
    res = Solution().findPeakGrid(mat = [[10,20,15],[21,30,14],[7,16,32]])
    print(res)
