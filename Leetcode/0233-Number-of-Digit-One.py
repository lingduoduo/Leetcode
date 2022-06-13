class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        m = 1
        while m < n + 1:
            a = n // m
            b = n % m
            res += (a + 8) // 10 * m + (b + 1 if a % 10 == 1 else 0)
            m = m * 10
        return res
        