class Solution:
    def monkeyMove(self, n: int) -> int:
        res, base, mod = 1, 2, 10**9 + 7
        while n > 0:
            if n % 2 == 1:
                res = (res * base) % mod
            base = (base * base) % mod
            n >>= 1
        return int((res - 2 + mod) % mod)
