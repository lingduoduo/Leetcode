class Solution:
    def integerReplacement(self, n: int) -> int:
        # print(n)
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n//2)
        else:
            return 1 + min(self.integerReplacement(n-1), self.integerReplacement(n+1))

if __name__ == '__main__':
    n = 8
    res = Solution().integerReplacement(n)
    print(res)
