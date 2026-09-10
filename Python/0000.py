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
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def check(start, end):
            if start > end:
                return False
            if s[start] == "0" and start != end:
                return False

            num = int(s[start : end + 1])
            return 0 <= num < 256

        def dfs(idx, path):
            if idx == len(s) and len(path) == 4:
                res.append(".".join(path))
                return

            if len(path) >= 4:
                return False

            for i in range(idx, len(s)):
                if check(idx, i):
                    dfs(i + 1, path + [s[idx : i + 1]])

        dfs(0, [])
        return res


if __name__ == "__main__":
    res = Solution().restoreIpAddresses(s="25525511135")
    print(res)
