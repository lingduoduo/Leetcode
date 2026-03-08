import heapq
from typing import List, Optional, Tuple, Optional
from collections import defaultdict, deque, Counter
import math

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ch in path.split('/'):
            if ch == ".":
                continue
            elif ch == "..":
                if stack:
                    stack.pop()
            elif ch:
                stack.append(ch)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    res = Solution().simplifyPath("/home/user/Documents/../Pictures")
    print(res)