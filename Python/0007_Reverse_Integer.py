class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= -(2**31) or x >= 2**31 - 1:
            return 0
        if x < 0:
            ind = -1
        else:
            ind = 1
        x = abs(x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        if res < -(2**31) or res > 2**31 - 1:
            return 0
        return ind * res


class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        x = x * flag

        res = int("".join(list(str(x))[::-1])) * flag
        return 0 if res <= -(2**31) or res >= 2**31 - 1 else res


class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        x = x * flag
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
            res = 0 if res <= -(2**31) or res >= 2**31 - 1 else res
        res = flag * res
        return res


if __name__ == "__main__":
    numbers = -123
    results = Solution().reverse(numbers)
    print(results)
