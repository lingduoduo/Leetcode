class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy = [0] * len(prices)
        buy[0] = prices[0]
        sell = [0] * len(prices)
        sell[0] = 0
        for i in range(1, len(prices)):
            buy[i] = min(buy[i - 1], prices[i])
            sell[i] = max(sell[i - 1], prices[i] - buy[i - 1])
        return sell[len(prices) - 1]
