from sortedcontainers import SortedList
from typing import List
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        sl = SortedList(nums[1 : 1 + dist])
        cursum, minsum = sum(sl[: k - 2]), float('inf')
        for i in range(1 + dist, n):
            if sl.bisect(nums[i]) <= k - 2:
                cursum += nums[i]
            else:
                cursum += sl[k - 2]
            minsum = min(minsum, cursum)
            sl.add(nums[i])
            if sl.bisect(nums[i - dist]) <= k - 2:
                cursum -= nums[i - dist]
            else:
                cursum -= sl[k - 2]
            sl.remove(nums[i - dist])
        return nums[0] + minsum
