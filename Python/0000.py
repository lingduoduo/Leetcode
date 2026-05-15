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
    def restoreIpAddresses(self, s: str) -> List[str]:

        def check(start, end):
            if start > end: return False
            if start == "0" and start != end: return False
            num = int(s[start: end + 1])
            return 0 <= num < 256
        
        def dfs(idx, path):
            if idx == len(s) and len(path) == 4:
                return '.'.join(res)
            
            if len(path) > 4:
                return 
            
            for i in range(idx, min(idx+3, len(s))):
                if check(idx, i):
                    dfs(i + 1, path + [s[idx: i+1]])
        
        res = []
        dfs(0)
        return None

if __name__ == "__main__":
    print(Solution().getMinimumDifference()))