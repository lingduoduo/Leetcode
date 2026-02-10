from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math

# class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    #     res = 0
    #     for i in range(len(arr)):
    #         for  j in range(i + 1):
    #             res = max(res, len(set(arr[i] + arr[j])))
    #     return res


class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: v for i, v in enumerate(nums) if v != 0}
    
    def prod(self, vec: "SparseVector"):
        res = 0
        if len(vec.d.keys) <= len(self.d):
            small = vec.d
            large = self.d
        else:
            small = self.d
            large = vec.d
        for i in small:
            if i in large:
                res += small[i] * large[i]
        return res
        



if __name__ == "__main__":
    res = Solution().subarraySum(nums = [1,2,3], k = 3)
    print(res)




