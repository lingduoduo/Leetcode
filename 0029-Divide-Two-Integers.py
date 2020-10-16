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
        

        ###https: // blog.csdn.net / L141210113 / article / details / 88306238?utm_medium = distribute.pc_relevant.none - task - blog - baidujs - 7 & spm = 1001.2101
# class Solution(object):
#     def divide(self, dividend, divisor):
#         res, flag = 0, 1
#         if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
#             flag = -1
#         dividend = abs(dividend)
#         divisor = abs(divisor)

#         while (dividend >= divisor):
#             times = 0
#             while (dividend >= divisor << times):
#                 times += 1
#             res += 1 << (times - 1)
#             dividend -= (divisor << (times - 1))

#         res = -res if flag < 0 else res

#         if res < -2147483648 or res > 2147483647:
#             return 2147483647

#         return res
import sys
sys.setrecursionlimit(10**6) 

class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = pow(2, 31) - 1
        MIN_INT = -pow(2, 31)
        
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        while dividend >= divisor:
            part = divisor
            cnt = 1
            while part + part <= dividend:
                part += part
                cnt += cnt
            dividend -= part
            res += cnt
        if res * sign >= MAX_INT:
            return MAX_INT
        if res * sign <= MIN_INT:
            return MIN_INT
        return res * sign
        
if __name__ == '__main__':
    # result = Solution().divide(-10, 10)
    result = Solution().divide(-2147483648, -1)
    # result = Solution().divide(7, -3)
    print(result)
