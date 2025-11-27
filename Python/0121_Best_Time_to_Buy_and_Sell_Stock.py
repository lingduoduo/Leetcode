from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        cur_min = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return res


if __name__ == "__main__":
    res = Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4])
    print(res)
