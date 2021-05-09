class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        ###first try
        ###d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #
        ###result = d[s[0]]
        ###for i in range(1, len(s)):
        ###    if d[s[i - 1]] >= d[s[i]]:
        ###        result += d[s[i]]
        ###    else:
        ###        result = result + d[s[i]] - 2 * d[s[i - 1]]
        ###return result
        
        ###second try
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i>0 and d[s[i]] > d[s[i-1]]:
                res += d[s[i]] - 2 * d[s[i-1]]
            else:
                res += d[s[i]]
        return res

if __name__=="__main__":
    print(Solution().romanToInt("III"))
