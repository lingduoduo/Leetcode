from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        self.par[rx] = ry
        # union by size
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        self.size[rx] += self.size[ry]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        uf = UnionFind(len(nums))
        index = {v: i for i, v in enumerate(nums)}
        for v in nums:
            if v + 1 in index:
                uf.union(index[v], index[v + 1])
        return max(uf.size)

if __name__ == "__main__":
    res = Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
    print(res)