class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        f = -1 if x < 0 else 1
        x = f * x
        while x:
            res = res * 10 + x % 10
            res = 0 if res <= -2**31 or res >= 2**31-1 else res
            x = x // 10
        return res * f

if __name__ == "__main__":
    res = Solution().reverse(x = 123)
    print(res)