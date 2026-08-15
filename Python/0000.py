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


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class UF:
    def __init__(self, n):
        self.par = list(range(1 + n))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return False
        self.par[par_x] = par_y
        return True


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = defaultdict(set)
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i + 1 :]):
                d[v1 + v2].add((v1, v2))

        res = set()
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i + 1 :]):
                val = target - (v1 + v2)
                if val in d:
                    for v3, v4 in d[val]:
                        res.add(tuple(sorted([v1, v2, v3, v4])))
        return res

        # res = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target - nums[i] - nums[j] in d:
        #             res.append([nums[i], nums[j]] + d[])


if __name__ == "__main__":
    res = Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
    print(res)
