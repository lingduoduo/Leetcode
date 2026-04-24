from collections import defaultdict, deque
from typing import List
import math
import heapq
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

if __name__ == "__main__":
    print(Solution().minAbsoluteDifference(nums = [4,3,2,4], x = 2))
