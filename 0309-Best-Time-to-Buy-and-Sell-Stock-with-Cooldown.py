class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        prev = 0
        curr = 0
        hold = -price[0]

        for i in range(1, len(prices)):
        	tmp = curr
        	curr = max(curr, hold + prices[i])
        	hold = max(hold, (prev if i>=2 else 0) - prices[i])
        	prev = tmp
        return curr


    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        rest = 0
        hold = float("-inf")

        for i in range(len(prices)):
        	prev_sold = sold
        	sold = hold+prices[i]
        	hold = max(hold, rest-price[i])
        	rest = max(rest, prev_sold)
        return max(rest, sold)