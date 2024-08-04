from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float("-inf")
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return sell


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]  # 持股票
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return max(dp[-1][0], dp[-1][1])
