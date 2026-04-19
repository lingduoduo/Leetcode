from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]

        for price in prices[1:]:
            res = max(res, price - min_price)
            min_price = min(min_price, price)
        return res





if __name__ == "__main__":
    res = Solution().maxProfit(prices = [7,1,5,3,6,4])
    print(res)
