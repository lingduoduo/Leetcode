class Solution(object):
    def maxProfit(self, prices):
        cur = prices[0]
        res = float("-inf")

        for price in prices[1:]:
            cur = min(cur, price)
            res = max(res, price - cur)
        return res

if __name__ == '__main__':
    res = Solution().maxProfit(prices=[9,11,8,5, 7, 12, 16, 14])
    print(res)

