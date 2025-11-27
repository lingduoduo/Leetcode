from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        @lru_cache(None)
        def rec(i):
            if i == n:
                return 0
            j = i + 1
            while j < n and jobs[i][1] > jobs[j][0]:
                j += 1
            one = jobs[i][2] + rec(j)
            two = rec(i + 1)
            return max(one, two)

        return rec(0)
