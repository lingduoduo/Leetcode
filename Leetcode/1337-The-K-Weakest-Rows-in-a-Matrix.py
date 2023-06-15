from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        stack = []
        res = []
        for idx, row in enumerate(mat):
            heapq.heappush(stack, (sum(row), idx))
        for i in range(k):
            tot, idx = heapq.heappop(stack)
            res.append(idx)
        return res
