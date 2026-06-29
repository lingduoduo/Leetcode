from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        que = deque([])
        for k, v in g.items():
            if len(v) == 1:
                que.append(k)
        
        remain = n
        while remain > 2:
            size = len(que)
            remain -= size

            for _ in range(size):
                leaf = que.popleft()
                nei = g[leaf].pop()
                g[nei].remove(leaf)

                if len(g[nei]) == 1:
                    que.append(nei)
        return list(que)
        

if __name__ == "__main__":

