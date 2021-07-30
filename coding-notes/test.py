class Solution:
    def NumberOf1(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n = n & (n - 1)
        return res


if __name__ == '__main__':
    res = Solution().NumberOf1(15)
    print(res)
