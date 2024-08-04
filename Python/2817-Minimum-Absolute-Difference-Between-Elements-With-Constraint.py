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