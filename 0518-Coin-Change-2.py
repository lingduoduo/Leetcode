class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[j] += dp[j - coins[i]]
        return dp[-1]
