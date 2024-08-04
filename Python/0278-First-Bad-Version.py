###The isBadVersion API is already defined for you.
###@param version, an integer
###@return a bool
###def isBadVersion(version):


def isBadVersion(selfself, n):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left


class Solution(object):
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
