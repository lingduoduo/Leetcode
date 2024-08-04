import itertools
import random


class Solution:
    def __init__(self, w: List[int]):
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i - 1] + w[i]

    def pickIndex(self) -> int:
        return bisect.bisect(self.preSum, self.preSum[-1] * random.random())
        # total = self.preSum[-1]
        # rand = random.randint(0, total - 1)
        # left, right = 0, len(self.preSum) - 1
        # while left + 1 < right:
        #     mid = (left + right) // 2
        #     if rand >= self.preSum[mid]:
        #         left = mid
        #     else:
        #         right = mid
        # if rand < self.preSum[left]:
        #     return left
        # return right


import numpy as np


class Solution:
    def __init__(self, w: List[int]):
        self.psum = [w[0]]
        for n in w[1:]:
            self.psum.append(self.psum[-1] + n)

    def pickIndex(self) -> int:
        def search(n):
            l, r = 0, len(self.psum)
            while l < r:
                m = (l + r) // 2
                if self.psum[m] <= n:
                    l = m + 1
                else:
                    r = m
            return l

        num = random.randint(0, self.psum[-1] - 1)
        return search(num)


class Solution:
    def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# return bisect.bisect(self.sum, num)
# return bisect.bisect(self.sum, self.sum[-1] * random.random())
