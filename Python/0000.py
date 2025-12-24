from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect

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
        
if __name__ == "__main__":
    res = Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
    print(res)

