class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i * i < x:
            i += 1
        if i * i == x:
            return i
        else:
            return i - 1


class Solution(object):
    def mySqrt(self, x):
        L = 0
        R = x
        while L <= R:
            mid = (L + R) // 2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                R = mid - 1
            else:
                L = mid + 1
        return R


class Solution(object):
    def mySqrt(self, x):
        L = 0
        R = x + 1
        while L < R:
            mid = L + (R - L) // 2
            if mid**2 <= x:
                L = mid + 1
            else:
                R = mid
        return L - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2 + 1
        ###[left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid**2 == x:
                return mid
            if mid**2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1
