class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if s == "1":
            return True
        if s == '0':
            return False
        
        ones = 0
        zeros = 0
        max_ones = 0
        max_zeros = 0
        for idx, cha in enumerate(s):
            if idx > 0 and cha == s[idx-1]:
                if cha == "1":
                    ones += 1
                else:
                    zeros += 1
            else:
                max_ones = max(max_ones, ones)
                max_zeros = max(max_zeros, zeros)
                ones = 0
                zeros = 0
        max_ones = max(max_ones, ones)
        max_zeros = max(max_zeros, zeros)

        if max_ones > max_zeros:
            return True
        else:
            return False