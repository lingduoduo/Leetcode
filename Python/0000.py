from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def pivotsort(nums):
            if len(nums) <= 1: return nums

            pivot = random.choice(nums)
            l, m, r = [], [], []

            for num in nums:
                if int(str(num) + str(pivot)) < int(str(pivot) + str(num)):
                    l.append(num)
                elif int(str(num) + str(pivot)) == int(str(pivot) + str(num)):
                    m.append(num)
                else:
                    r.append(num)
            return pivotsort(l) + m + pivotsort(r)

        nums = pivotsort(nums)[::-1]
        strs = list(map(str, nums))  
        return ''.join(strs)
    

if __name__ == "__main__":
    res = Solution().largestNumber(nums = [3,30,34,5,9])
    print(res)

