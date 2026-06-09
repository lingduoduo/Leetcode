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
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces = [0] + spaces + [len(s)]
        for i, v in enumerate(spaces[:-1]):
            start = spaces[i]
            end = spaces[i + 1]
            res.append(s[start: end])
        return ' '.join(res)
    






if __name__ == "__main__":
    res = Solution().addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15])
    print(res)
