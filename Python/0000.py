from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prev = 0
        res = 1
        for i in range(1, len(nums)):
            cur = nums[i] - nums[i-1]
            if (prev >= 0 and cur <= 0) or (prev <= 0 and cur >= 0):
                res += 1
                prev = cur
        return res


if __name__ == "__main__":
    print(Solution().wiggleMaxLength(nums = [1,17,5,10,13,15,10,5,16,8]))