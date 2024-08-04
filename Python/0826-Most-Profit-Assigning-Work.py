from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(profit, difficulty), reverse=True)
        worker.sort()
        res = 0

        for prof, diff in jobs:
            while worker and diff <= worker[-1]:
                res += prof
                worker.pop()
            if not worker:
                break
        return res
