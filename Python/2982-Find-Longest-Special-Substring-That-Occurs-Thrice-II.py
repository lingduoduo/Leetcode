class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        d = defaultdict(list)
        l = 0
        while l < n:
            r = l
            while r<n and s[l] == s[r]:
                r+=1
            for i in range(r-l,max(0,r-l-4),-1):
                d[s[l]].append(i)    
            l = r 
            
        res = -1
        for key in d:
            if len(d[key]) >= 3:
                res = max(res,sorted(d[key])[-3])
        return res  