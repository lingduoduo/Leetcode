class Solution:
    def magicalString(self, n: int) -> int:
        S = [1, 2, 2]
        i = 2
        curr = 1
        while i < n:
            S += [curr] * S[i]
            curr = 2 if curr == 1 else 1
            i += 1
        return S[:n].count(1)
