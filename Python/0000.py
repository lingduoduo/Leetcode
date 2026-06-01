from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        strs = list(str(n))

        m = len(strs)
        i = m - 1
        while i > 0 and strs[i - 1] >= strs[i]:
            i -= 1
        if i == 0 : 
            return -1
        
        j = m - 1
        while j > i - 1 and strs[j] <= strs[i - 1]:
            j -= 1
        
        strs[j], strs[i - 1] = strs[i - 1], strs[j]
        strs[i:] = strs[i:][::-1]
        num = int(''.join(strs))
        return res if res < 2**31 else -1

        



                
if __name__ == "__main__":
    res = Solution().maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)
    print(res)
