from typing import List
import heapq
import collections
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        dp = [float("-inf")] * len(nums)
        dp[0] = nums[0]
        max_heap = []
        heapq.heappush(max_heap, (-nums[0], 0))

        for i in range(1, len(nums)):
            while max_heap[0][1] < i - k:
                heapq.heappop(max_heap)
            dp[i] = nums[i] - max_heap[0][0]
            heapq.heappush(max_heap, (-dp[i], i))

        return dp[-1]


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float(-inf)] * len(nums)
        dp[0] = nums[0]
        dq = collections.deque()
        dq.append(0)

        for i in range(1, len(nums)):
            # similar to liding window maximum
            while dq and dq[0] < i - k:
                dq.popleft()
            dp[i] = nums[i] + dp[dq[0]]
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return dp[-1]

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = nums[0]
        dq = deque()
        dq.append((0, score))
        for i in range(1, n):
            # pop the old index
            while dq and dq[0][0] < i-k:
                dq.popleft()
            score = dq[0][1] + nums[i]
            # pop the smaller value
            while dq and score >= dq[-1][1]:
                dq.pop()
            dq.append((i, score))
        return score