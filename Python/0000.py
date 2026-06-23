from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        res = 0
        zeros = 0
        for i, v in enumerate(nums):
            if v == 0:
                zeros += 1
                while zeros > k:
                    if nums[start] == 0:
                        zeros -= 1
                    start += 1
            res = max(res, i - start + 1)
        return res
        


if __name__ == "__main__":
    res = Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
    print(res)
