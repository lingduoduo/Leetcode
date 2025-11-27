class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N

        F = [0] * (1 + N)

        F[1] = 1
        for i in range(2, 1 + N):
            F[i] = F[i - 1] + F[i - 2]

        return F[N]
