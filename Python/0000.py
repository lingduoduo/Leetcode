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
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            if idx > len(nums):
                return
            elif len(path) >= 2:
                res.append(path)

            visited = set()
            for i in range(idx, len(nums)):
                if nums[i] in visited:
                    continue
                if len(path) == 0:
                    visited.add(nums[i])
                    dfs(i + 1, path + [nums[i]])
                elif path and path[-1] <= nums[i]:
                    if path + [nums[i]]:
                        visited.add(nums[i])
                        dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res


if __name__ == "__main__":
    res = Solution().findSubsequences(nums=[4, 6, 7, 7])
    print(res)
