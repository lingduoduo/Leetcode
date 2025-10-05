class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                sub = s[:i]
                times = len(s) // i
                if sub * times == s:
                    return True
        return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        next = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        
        len_repeated = next[-1]
        repeating_unit_length = n - len_repeated
        if len_repeated > 0 and n % repeating_unit_length == 0:
            return True
        return False


if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern("abab"))
