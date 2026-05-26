from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intervals = firstList + secondList     
        intervals.sort(key=lambda x: (x[0], x[1]))
        stack = [intervals[0]]
        res = []
        for x, y in intervals[1:]:
            px, py = stack[-1]
            if x <= py:
                res.append([max(x, px), min(y, py)])
            stack.append([x, y])
        return res

if __name__ == "__main__":
    res = Solution().intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])
    print(res)
