class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        while n > 0:
            if n % 2 == 1:
                result += 1
            n = n // 2

        return result


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


if __name__ == "__main__":
    res = Solution().hammingWeight(int("11111111111111111111111111111101", 2))
    print(res)
