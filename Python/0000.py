from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# if __name__ == "__main__":
#     print(Solution().findSubsequences())