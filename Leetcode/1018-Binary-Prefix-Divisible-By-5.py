class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        num = 0

        for i in range(len(A)):
            num = num * 2 + A[i]
            res.append(num % 5 == 0)
        return res
