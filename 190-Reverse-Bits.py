# class Solution:
    # @param n, an integer
    # @return an integer
    # def reverseBits(self, n):
    #     if n == 0:
    #         return 0
    #     bits = self.intToBit(n)
    #     return self.bitToInt(bits[::-1])
    #     # return bits
    #
    # def intToBit(self, n):
    #     bits = ''
    #     while (n > 0):
    #         bits = str(n % 2) + bits
    #         n = n // 2
    #     while len(bits) < 32:
    #         bits = '0' + bits
    #     return bits
    #
    # def bitToInt(self, bits):
    #     res = 0
    #     for i in range(len(bits)):
    #         if bits[i] == '1':
    #             res = res * 2 + 1
    #         else:
    #             res = res * 2
    #     return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res
        

if __name__ == '__main__':
    n = 43261596
    result = Solution().reverseBits(n)
    print(result)
