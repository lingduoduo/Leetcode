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


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)

        for s, e, v in roads:
            g[s].append((v, e))
            g[e].append((v, s))

        que = deque([1])
        visited = {1}
        res = float("inf")
        while que:
            node = que.popleft()

            for v, nei in g[node]:
                res = min(res, v)

                if nei not in visited:
                    visited.add(nei)
                    que.append(nei)

        return res


if __name__ == "__main__":
    res = Solution().minScore(n=4, roads=[[1, 2, 2], [1, 3, 4], [3, 4, 7]])
    print(res)
