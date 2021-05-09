class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        d, m = divmod(k - n, 25)
        return "a" * (n - 1 - d) + (chr(m + 97) if d != n else "") + "z" * d