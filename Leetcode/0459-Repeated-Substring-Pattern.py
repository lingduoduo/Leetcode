class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                sub = s[:i]
                times = len(s) // i
                if sub * times == s:
                    return True
        return False
