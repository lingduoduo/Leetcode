class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        n = int(c ** (1 / 2.0) + 1)
        for i in range(n):
            a = int((c - i * i) ** (1 / 2.0))
            if i * i + a * a == c:
                return True
        return False
