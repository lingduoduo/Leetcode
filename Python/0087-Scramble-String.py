class Solution:
    @lru_cache(maxsize=None)  # optional
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        # important, TLE if commneted out
        if Counter(s1) != Counter(s2):
            return False
        L = len(s1)
        for l in range(1, L):
            if self.isScramble(s1[0:l], s2[0:l]) and self.isScramble(s1[l:], s2[l:]):
                return True
            if self.isScramble(s1[0:l], s2[L - l :]) and self.isScramble(
                s1[l:], s2[0 : L - l]
            ):
                return True
        return False
