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


class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.minstack.append(value)
        else:
            self.stack.append(value)
            self.stack.append(min(value, self.minstack[-1]))

    def pop(self) -> None:
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# if __name__ == "__main__":
#     res = Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
#     print(res)
