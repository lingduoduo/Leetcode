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

class Solution:
    def countDigitOne(self, n: int) -> int:
        m = len(str(n))
        if m == 1:
            return 0 if n == 0 else 1
        num_digits_tenth = (m - 1) * 10 ** (m - 1)
        num_ones_tenth = num_digits_tenth // 10
        first_digit = n // (10 ** (m-1))
        rest = n % (10 ** (m-1))
        if first_digit > 1:
            return num_ones_tenth * first_digit + (10 ** (m - 1)) + self.countDigitOne(rest)
        else:
            return num_ones_tenth + self.countDigitOne(rest) + (rest + 1)
