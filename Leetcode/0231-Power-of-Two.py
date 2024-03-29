class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ###if n <= 0: return False
        #
        ###i = int(math.log(n, 2))
        ###if 2 ** i == n:
        ###    return True
        ###else:
        ###    return False

        if n < 1:
            return False

        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count("1") == 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
