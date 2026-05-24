from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [set()]
        for word in arr:
            if len(set(word)) < len(word):
                continue
            word = set(word)
            for prev in res:
                if prev & word:
                    continue
                res.append(prev | word)
        return max(map(len, res))

if __name__ == "__main__":
    res = Solution().maxLength(arr = ["un","iq","ue"])
    print(res)
