class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f=dict()
        # f[0]=1
        # f[1]=1
        # for i in range(2, n+1):
        # 	f[i] = f[i-1] + f[i-2]
        # return f[n]
        
        ## second try
        f = [1] * (n + 1)
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]
        
        # return 1 if n<=1 else self.climbStairs(n-1)+self.climbStairs(n-2)


if __name__ == "__main__":
    result = Solution().climbStairs(10)
    print(result)
