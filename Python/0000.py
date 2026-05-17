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
    def isNumber(self, s: str) -> bool:
        digit = exponent = dot = False
        for i, ch in enumerate(s):
            if ch.isdigit():
                digit = True
            elif ch in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif ch in 'eE':
                if exponent or not digit:
                    return False
                exponent = True
                digit = False
            elif ch == '.':
                if dot or exponent: 
                    return False
                dot = True
            else:
                return False
        return digit

            




# if __name__ == "__main__":
#     print(Solution().getMinimumDifference()))