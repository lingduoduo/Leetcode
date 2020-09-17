class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        t = s.count('1')
        if t % 3 != 0: 
            return 0
        if t == 0: 
            return ((n - 1) * (n - 2) // 2) % (10**9 + 7)
        t //= 3
        l, r, c = 0, 0, 0
        for i, ch in enumerate(s):
            if ch == '1': 
                c += 1
            if c == t: 
                l += 1
            elif c == t * 2: 
                r += 1
        return (l * r) % (10**9 + 7)   