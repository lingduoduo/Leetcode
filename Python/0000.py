from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i-1]:
                res[i] = res[i - 1] + 1
        for i in range(n, -1, -1):
            if i < n - 2 and ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)              


if __name__ == "__main__":
    res = Solution().candy(ratings = [1,0,2])

    print(res)
