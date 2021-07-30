class Solution:
    def totalMoney(self, n: int) -> int:
        t, r = divmod(n, 7)
        res = 0
        for i in range(1, t + 1):
            res += sum(range(i, i + 7))
        res += sum(range(t + 1, t + r + 1))
        return res

if __name__ == '__main__':
    res = Solution().totalMoney(n=20)
    print(res)