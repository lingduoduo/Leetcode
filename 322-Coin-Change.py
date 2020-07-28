class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp = [float('inf') * (amount + 1)]
        #
        # dp[0] = 0
        #
        # for i in range(len(coins)):
        #     for j in range(coins[i], amount + 1):
        #         dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        # return -1 if dp[-1] == float(-1) else dp[-1]
        
        dp = [0] + [-1]*len(amount)
        
        for x in range(len(amount)):
            if dp[x] < 0:
                continue
                
            for c in coins:
                if x+c > amount:
                    continue
                if dp[x+c] < 0 or dp[x+c] > dp[x]+1:
                    dp[x+c] = dp[x]+1
        return dp[amount]
        
            
