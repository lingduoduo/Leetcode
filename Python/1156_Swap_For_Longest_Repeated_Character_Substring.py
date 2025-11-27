from collections import Counter
from itertools import groupby

class Solution:

    def maxRepOpt1(self, text: str) -> int:                     #  Example:  text = "babbab"

        c = Counter(text)                                       #               c = {'a':2, 'b':4}

        ch, ct = zip(*[(k, sum(1 for _ in g))                   #              ch = ('b','a','b','a','b')
                       for k, g in groupby(text)])              #              ct = ( 1 , 1 , 2 , 1 , 1 )

        n = len(ch)
        
        res = max(ct[i]+(ct[i]<c[ch[i]]) for i in range(n))     #          ans = max (2 , 2,  3,  2,  2 ) = 3

        for i in range(1, n-1):                                 #       i     sm+(sm<c[ch[i-1]])    ans
                                                                #    –––––––  ––––––––––––––––––    –––
            if ch[i-1] == ch[i+1] and ct[i] == 1:               #       0                            3
                sm = ct[i-1]+ct[i+1]                            #       1       3 + (3 < 4) = 4      4
                res = max(res, sm + (sm < c[ch[i-1]]))          #       2                            4
                                                                #       3       3 + (3 < 4) = 4      4
        return res                                              #       4                            4 <–– return

if __name__ == '__main__':
    res = Solution().maxRepOpt1("ababa")
    print(res)

