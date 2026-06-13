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
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)

        for s, e in tickets:
            g[s].append(e)

        for s in g:
            g[s].sort(reverse=True)

        stack = ["JFK"]
        res = []

        while stack:
            while g[stack[-1]]:
                stack.append(g[stack[-1]].pop())
            res.append(stack.pop())

        return res[::-1]








if __name__ == "__main__":
    res = Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    print(res)
