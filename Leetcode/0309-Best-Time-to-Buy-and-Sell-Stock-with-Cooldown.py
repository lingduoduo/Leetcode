from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        prev = 0
        curr = 0
        hold = -price[0]

        for i in range(1, len(prices)):
            tmp = curr
            curr = max(curr, hold + prices[i])
            hold = max(hold, (prev if i >= 2 else 0) - prices[i])
            prev = tmp
        return curr


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0  ## before buy status
        cooldown = 0  ## after sell status
        hold = -prices[0]  ## before sell status

        for i in range(1, len(prices)):
            prev_profit = profit
            profit = hold + prices[i]  ## sell
            hold = max(hold, cooldown - prices[i])  ## buy
            cooldown = max(cooldown, prev_profit)

        return max(cooldown, profit)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("-inf")
        pre_buy = 0
        sell = 0
        pre_sell = 0

        for i in range(len(prices)):
            pre_buy = buy
            buy = max(pre_buy, pre_sell - prices[i])
            pre_sell = sell
            sell = max(pre_sell, pre_buy + prices[i])
        return sell
