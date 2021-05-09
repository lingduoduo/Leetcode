class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na, nb = len(a), len(b)
        times = nb // na + 3
        for i in range(1, times):
            if b in a * i:
                return i
        return -1
   