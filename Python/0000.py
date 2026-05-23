from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maximumSwap(self, num: int) -> int:
        strs =list(str(num))
        
        n = len(strs)
        r, idx = n - 2, n - 1
        while r >= 0:
            if strs[r] > strs[idx]:
                idx = r
            r -= 1
            
        if idx == 0: return num

        l = 0
        while l > r and strs[l] < strs[r]:
            l += 1
        strs[l], strs[r] = strs[r], strs[l]
        return int(''.join(strs))

if __name__ == "__main__":
    res = Solution().maximumSwap(num = 2736)
    print(res)
