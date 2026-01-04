from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_left(root)
    
    # Push all left children starting from node
    def push_left(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        if node.right:
            self.push_left(node.right)
        return val
    
    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
    
if __name__ == "__main__":
    res = Solution().kthFactor(n = 12, k = 3)
    print(res)
