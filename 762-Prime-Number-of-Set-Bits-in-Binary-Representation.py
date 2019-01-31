class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def bits_set(n):
        	bits = 0
        	while n>0:
        		if n%2 == 1:
        			bits += 1
        		n=n//2
        	return bits

        def is_prime(n):
        	if n==1: return False
        	if n==2: return True
        	for i in range(2, n):
        		if n%i == 0: 
        			return False
        	return True

        result = 0
        for i in range(L, R+1):
        	t = bits_set(i)
        	if is_prime(t):
        		result += 1
        return result
