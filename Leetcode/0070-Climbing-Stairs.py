class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ###f=dict()
        ###f[0]=1
        ###f[1]=1
        ###for i in range(2, n+1):
        ###	f[i] = f[i-1] + f[i-2]
        ###return f[n]
        
        ####second try
        ###f = [1] * (n + 1)
        ###for i in range(2, n + 1):
        ###    f[i] = f[i - 1] + f[i - 2]
        ###return f[n]
        
        ###return 1 if n<=1 else self.climbStairs(n-1)+self.climbStairs(n-2)

        # f = {}
        # f[0] = 1
        # f[1] = 1
        # i=2
        # while i<=n:
        #     f[i] = i+f[i-1]
        #     i += 1
        # return f[n]

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
            
if __name__ == "__main__":
    result = Solution().climbStairs(2)
    print(result)
