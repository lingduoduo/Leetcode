class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ####二分求幂
        if n==0:
        	return 1

        if n<0:
        	x = 1/x
        	n = -n
        if n%2:
        	return x*self.myPow(x, n-1)
        retrun self.myPow(x*x, n/2)

