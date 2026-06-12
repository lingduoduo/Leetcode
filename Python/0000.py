from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        cur = 1
        que = deque([root])
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if cur == depth - 1:
                    old_left = node.left
                    old_right = node.right

                    node.left = TreeNode(val)
                    node.left.left = old_left

                    node.right = TreeNode(val)
                    node.right.right = old_right
                    return root
                else:
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            cur += 1
        return root





if __name__ == "__main__":
    res = Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]])
    print(res)
