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


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort jobs by start time
        jobs = sorted(zip(startTime, endTime, profit))  # (s, e, p)
        n = len(jobs)
        starts = [s for s, _, _ in jobs]

        # nxt[i] = first index j > i such that jobs[j].start >= jobs[i].end
        nxt = [n] * n
        for i in range(n):
            e = jobs[i][1]
            nxt[i] = bisect.bisect_left(starts, e)

        dp = [0] * (n + 1)  # dp[i] = max profit from jobs[i:]
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], jobs[i][2] + dp[nxt[i]])

        return dp[0]