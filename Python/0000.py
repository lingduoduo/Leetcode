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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def __init__(self, w: List[int]):
        self.w = [w[0]]
        for v in w[1:]:
            self.w.append(self.w[-1] + v)
        self.tot = self.w[-1]

    def pickIndex(self) -> int:
        target = self.tot * random.random()
        l, r = 0, len(self.w)
        while l < r:
            m = l + (r - l) // 2
            if self.w[m] < target:
                l = m + 1
            else:
                r = m
        return l


if __name__ == "__main__":
    res = Solution().copyRandomList(head=[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]])
    print(res)
