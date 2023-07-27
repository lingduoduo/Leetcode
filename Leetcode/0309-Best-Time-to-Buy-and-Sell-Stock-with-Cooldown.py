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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [
            [0] * 4 for _ in range(n)
        ]  # 创建动态规划数组，4个状态分别表示持有股票、不持有股票且处于冷冻期、不持有股票且不处于冷冻期、不持有股票且当天卖出后处于冷冻期
        dp[0][0] = -prices[0]  # 初始状态：第一天持有股票的最大利润为买入股票的价格
        for i in range(1, n):
            dp[i][0] = max(
                dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i]
            )  # 当前持有股票的最大利润等于前一天持有股票的最大利润或者前一天不持有股票且不处于冷冻期的最大利润减去当前股票的价格
            dp[i][1] = max(
                dp[i - 1][1], dp[i - 1][3]
            )  # 当前不持有股票且处于冷冻期的最大利润等于前一天持有股票的最大利润加上当前股票的价格
            dp[i][2] = (
                dp[i - 1][0] + prices[i]
            )  # 当前不持有股票且不处于冷冻期的最大利润等于前一天不持有股票的最大利润或者前一天处于冷冻期的最大利润
            dp[i][3] = dp[i - 1][2]  # 当前不持有股票且当天卖出后处于冷冻期的最大利润等于前一天不持有股票且不处于冷冻期的最大利润
        return max(dp[n - 1][3], dp[n - 1][1], dp[n - 1][2])  # 返回最后一天不持有股票的最大利润
