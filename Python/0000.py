from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:        
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if abs(tot - target) < abs(res - target):
                    res = tot
                if tot == target:
                    return tot
                elif tot < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res

if __name__ == "__main__":
    res = Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1)
    print(res)

