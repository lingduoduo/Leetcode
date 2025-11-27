class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        tot = s.count('1', 1)
        if s[0]=='0': 
            tot += 1
        res = tot
        for c in s[1:n-1]:
            if c=='0': 
                tot += 1
            else: 
                tot -= 1
            res = max(res, tot)
        return res