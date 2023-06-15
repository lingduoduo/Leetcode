# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         n = len(prices)
#         g = [[0] * 3 for _ in range(N)]
#         l = [[0] * 3 for _ in range(N)]
#         for i in range(1, n):
#             diff = prices[i] - prices[i - 1]
#             for j in range(1, 3):
#                 l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
#                 g[i][j] = max(l[i][j], g[i - 1][j])
#         return g[-1][-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # buy1[i] = max(buy1[i - 1], -prices[i])
        # sell1[i] = max(sell1[i - 1], buy1[i] + prices[i])
        # buy2[i] = max(buy2[i - 1], sell1[i - 1] - prices[i])
        # sell2[i] = max(sell2[i - 1], buy2[i] + prices[i])

        sell1 = sell2 = 0
        buy1 = buy2 = -float("inf")
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2
