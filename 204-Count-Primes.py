class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        f = [1] * n
        f[0] = f[1] = 0
        
        for i in range(2, int(n ** (1 / 2))):
            if not f[i]:
                continue
            j = 2
            while j * i < n:
                f[j * i] = 0
                j += 1
        return sum(f)
