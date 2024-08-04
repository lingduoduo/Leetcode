import math
import functools


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        cnt = 2
        for i in range(4, n + 1):
            if self.prime(i):
                cnt += 1
        return self.factorial(cnt) * self.factorial(n - cnt) % (pow(10, 9) + 7)

    def prime(self, n) -> bool:
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def factorial(self, n):
        return functools.reduce(lambda x, y: x * y, range(1, n + 1))

        # if n <= 1:
        #     return 1
        # return n * self.factorial(n - 1)


if __name__ == "__main__":
    # print(Solution().factorial(3))

    # print(Solution().prime(17))

    res = Solution().numPrimeArrangements(100)
    print(res)

    res = Solution().numPrimeArrangements(11)
    print(res)
