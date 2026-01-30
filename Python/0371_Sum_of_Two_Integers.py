import numpy as np


class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            a, b = np.int32(a ^ b), np.int32((a & b) << 1)
        return int(a)


import numpy as np


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        bit = 1

        while a or b or carry:
            a_bit = a & 1
            b_bit = b & 1

            s = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)

            res |= s * bit
            bit <<= 1
            a >>= 1
            b >>= 1

        return res  