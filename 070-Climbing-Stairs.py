class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=dict()
        f[0]=1
        f[1]=1
        for i in range(2, n+1):
        	f[i] = f[i-1] + f[i-2]
        return f[n]
        
