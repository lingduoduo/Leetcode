class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = pow(2, 31) - 1
        MIN_INT = -pow(2, 31)
        if dividend >= 0:
            sign1 = 1
        else:
            sign1 = -1
        dividend = sign1 * dividend

        if divisor >= 0:
            sign2 = 1
        else:
            sign2 = -1
        divisor = sign2 * divisor

        res = 0
        while dividend >= divisor:
            part = divisor
            cnt = 1
            while part + part <= dividend:
                part += part
                cnt += cnt
            dividend -= part
            res += cnt
        if res * sign1 * sign2 >= MAX_INT:
            return MAX_INT
        if res * sign1 * sign2 <= MIN_INT:
            return MIN_INT
        return res * sign1 * sign2


if __name__ == '__main__':
    result = Solution().divide(100, 10)
    result = Solution().divide(-2147483648, -1)
    result = Solution().divide(7, -3)
    print(result)
