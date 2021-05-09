class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        i = 0
        res = 1
        while i < len(s):
            j = i + 1
            tmp = 1
            while j < len(s) and s[j-1] == s[j]:
                tmp += 1
                j += 1
            res = max(res, tmp)
            i = j
        return res