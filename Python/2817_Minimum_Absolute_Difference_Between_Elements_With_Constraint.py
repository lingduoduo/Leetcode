import heapq
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sortedNums = sorted((nums[i], i) for i in range(len(nums)))
        heapLeft, heapRight = [], []
        minDiff = float('inf')

        for i in range(len(sortedNums)):
            val, index = sortedNums[i]
            heapq.heappush(heapLeft, (index, val))
            heapq.heappush(heapRight, (-index, val))


            while heapLeft and heapLeft[0][0] + x <= index:
                minDiff = min(minDiff, val - heapq.heappop(heapLeft)[1])
            while heapRight and heapRight[0][0] + x <= -index:
                minDiff = min(minDiff, val - heapq.heappop(heapRight)[1])
        return minDiff

import bisect
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        res = float("inf")
        sorted_list = []
        for i, num in enumerate(nums):
            if i >= x:
                bisect.insort(sorted_list, nums[i - x])
                pos = bisect.bisect_left(sorted_list, num)
                if pos > 0:
                    res = min(res, abs(num - sorted_list[pos - 1]))

                if pos < len(sorted_list):
                    res = min(res, abs(num - sorted_list[pos]))
        return res