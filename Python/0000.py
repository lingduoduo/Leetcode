import heapq
from typing import List, Optional, Tuple, Optional
from collections import defaultdict, deque, Counter
import math

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        costs = [0] + costs
        dp = [0] * (1 + n)
        dp[1] = costs[1] +  1
        dp[2] = min(costs[1] + dp[1], costs[2] + 2 ** 2)
        dp[3] = min(costs[2] + dp[1], costs[1] + dp[2], costs[3] + 3 ** 2)

        for i in range(4, n):
            dp[i] = min(costs[i - 1] + dp[i - 2], costs[i - 2] + dp[i - 1], costs[i - 3] + 3 ** 2)
        
        return dp[-1]

if __name__ == "__main__":
    res = Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 1)
    print(res)