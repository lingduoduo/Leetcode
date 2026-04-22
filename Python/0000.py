from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        presum = 0
        res = 0
        d = defaultdict(int)
        d[0] = 1
        for num in nums:
            if num % 2 == 1:
                presum += 1
            if presum - k in d:
                res += d[presum -k]
            d[presum] += 1
        return res
            
        
if __name__ == "__main__":
    print(Solution().numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
