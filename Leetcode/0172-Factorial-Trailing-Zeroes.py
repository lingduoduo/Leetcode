class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0:
            res += n//5
            n = n//5
        return res

if __name__ == "__main__":
    numbers = 5
    results = Solution().trailingZeroes(numbers)
    print(results)
