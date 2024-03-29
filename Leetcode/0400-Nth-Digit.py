###1   1-9
###2   10-99
###3   100-999
###4   1000-9999
###5   10000-99999
###6   100000-999999
###7   1000000-9999999
###8   10000000-99999999
###9   100000000-99999999


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range(9):
            d = 9 * pow(10, i)
            if n <= d * (i + 1):
                break
            n -= d * (i + 1)
        n -= 1
        return int(str(pow(10, i) + n / (i + 1))[n % (i + 1)])


class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 1
        digit_len = 1
        cnt = 9

        while n > digit_len * cnt:
            n -= digit_len * cnt
            start *= 10
            digit_len += 1
            cnt *= 10

        start += (n - 1) / digit_len
        return int(str(start)[(n - 1) % digit_len])
