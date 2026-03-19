from typing import List
import heapq
from collections import defaultdict
import random

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for num in nums:
            left.append(num * left[-1])
        left.pop(0)
        
        for num in nums[::-1]:
            right.append(num * right[-1])
        right = right[::-1]
        right.pop(0)
        
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res
        


if __name__ == "__main__":
    res = Solution().productExceptSelf(nums = [1,2,3,4])
    print(res)
