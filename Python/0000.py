from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)

        heap = []
        for i, v in d.items():
            heapq.heappush(heap, (v, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i for _, i in sorted(heap, key=lambda x: -x[0])]


if __name__ == "__main__":
    print(Solution().topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))