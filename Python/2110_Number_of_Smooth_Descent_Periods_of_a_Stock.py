from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        start = 0
        for i, v in enumerate(prices):
            if prices[start] - v == i - start:
                res += i - start + 1
            else:
                res += 1
                start = i
        return res
    
if __name__ == "__main__":
    res = Solution().getDescentPeriods(prices = [8,6,7,7,6])
    print(res)
