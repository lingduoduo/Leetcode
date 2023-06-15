class Solution:
    def bitwiseComplement(self, N: int) -> int:
        res = []
        while N > 0:
            res.append(1 - N % 2)
            N = N // 2
        res = res[::-1]
        print(res)

        output = 0
        for i in range(len(res)):
            output = output * 2 + res[i]
        return output


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        nums = list(bin(n)[2:][::-1])
        res = 1
        for i in range(len(nums)):
            res <<= 1
        res -= 1
        res ^= n
        return res


import numpy as np


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = (2 << int(np.log2(n))) - 1
        res ^= n
        return res


if __name__ == "__main__":
    results = Solution().bitwiseComplement(10)
    print(results)
