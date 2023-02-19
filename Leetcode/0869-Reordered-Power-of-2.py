import itertools
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        pow2 = []
        for i in range(31):
            pow2.append(''.join(sorted(list(str(2 ** i)))))
        return ''.join(sorted(list(str(n)))) in pow2

class Solution:
   def reorderedPowerOf2(self, n: int) -> bool:
       return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
           for cand in itertools.permutations(str(n)))

if __name__ == '__main__':
    res = Solution().reorderedPowerOf2(5)
    print(res)