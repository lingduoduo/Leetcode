class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0

        while m != n:
            m = m >> 1
            n = n >> 1
            i += 1
        return m << i
        