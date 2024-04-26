from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(list)
        l = 0
        while l < len(s):
            r = l
            while r <  len(s) and s[l] == s[r]:
                r += 1
            for i in range(r-l, max(0, r-l-4), -1):
                d[s[l]].append(i)    
                print(d)
            l = r 
            
        res = -1
        for key in d:
            if len(d[key]) >= 3:
                res = max(res,sorted(d[key])[-3])
        return res       

if __name__ == '__main__':
    obj = Solution()
    res = obj.maximumLength(s = "aaaa")
    print(res)
