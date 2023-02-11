class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ####二分求幂
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n % 2:
                res *= x
            n >>= 1
            x *= x
        return res
