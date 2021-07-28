class Solution:
    def Fibonacci(self, n) -> int:
        res = []
        res.append(0)
        res.append(1)
        for i in range(n-1):
            res.append(res[-1] + res[-2])
        print(res)
        return res[-1]


if __name__ == '__main__':
    res = Solution().Fibonacci(3)
    print(res)
