from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        res = 0
        x, y = 0, 0
        dx, dy = 0, 1
        for command in commands:
            if command == -2:      # turn left
                dx, dy = -dy, dx
            elif command == -1:    # turn right
                dx, dy = dy, -dx
            else:
                for _ in range(command):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obstacles:
                        break

                    x, y = nx, ny
                    res = max(res, x * x + y * y)
        return res








        

if __name__ == "__main__":
    print(Solution().getMinimumDifference()))