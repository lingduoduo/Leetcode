class Solution:
    def bitToInt(self, bits):
       res = 0
       for i in range(len(bits)):
           if bits[i] == '1':
               res = res * 2 + 1
           else:
               res = res * 2
       return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        return res

if __name__ == '__main__':
    n = 43261596
    result = Solution().reverseBits(n)
    print(result)
