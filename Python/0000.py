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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s:
                break

        if not f or not f.next:
            return None

        s = head
        while s != f:
            s = s.next
            f = f.next
        return s


if __name__ == "__main__":
    res = Solution().maximalSquare(matrix=[["0", "1"], ["1", "0"]])
    print(res)
