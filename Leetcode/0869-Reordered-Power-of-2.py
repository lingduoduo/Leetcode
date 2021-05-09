class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        pow2 = []
        for i in range(31):
            pow2.append(''.join(sorted(list(str(2 ** i)))))
        return ''.join(sorted(list(str(N)))) in pow2

if __name__ == '__main__':
    res = Solution().reorderedPowerOf2(5)
    print(res)