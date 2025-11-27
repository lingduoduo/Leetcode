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
