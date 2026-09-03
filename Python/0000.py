from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq
import random


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, v in enumerate(height):
            while stack and height[stack[-1]] < v:
                m = stack.pop()
                if stack:
                    h = min(v, height[stack[-1]]) - height[m]
                    w = i = stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res

        stack = []
        res = 0
        for i, v in enumerate(height):
            while stack and height[stack[-1]] < v:
                m = stack.pop()
                if stack:
                    h = min(height[stack[-1]], v) - height[m]
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res


if __name__ == "__main__":
    res = Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(res)
