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
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def dfs(idx, path):
            if len(path) == k:
                res.append(path)
                return

            for i in range(idx, n + 1):
                dfs(i + 1, path + [i])

        dfs(1, [])
        return res


if __name__ == "__main__":
    res = Solution().combine(n=1, k=1)
    print(res)
