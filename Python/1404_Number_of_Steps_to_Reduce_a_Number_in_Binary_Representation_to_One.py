class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        res = 0
        carry = 0
        for i in range(n - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                res += 2
                carry = 1
            else:
                res += 1

        return res + carry