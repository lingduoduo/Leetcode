from collections import defaultdict, deque
from typing import List
import math
import heapq

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (1 + n)
        for i in range(1 + n):
            dp[i] = dp[i//2] + i % 2
        return sum(dp)




if __name__ == "__main__":
    res = Solution().countBits(n = 5)
    print(res)
