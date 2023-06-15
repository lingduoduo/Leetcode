class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        result = n
        while result >= 0:
            l = list(str(result))
            result = 0

            while l:
                result += int(l.pop()) ** 2
            if result == 1 or result == 7:
                return True
            elif result < 10:
                return False


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            res = 0
            for c in list(str(n)):
                res += int(c) ** 2
            n = res
        return n == 1


if __name__ == "__main__":
    n = 1111111
    result = Solution().isHappy(n)
    print(result)
