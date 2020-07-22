class Solution(object):
    def intToRoman(self, num: int) -> str:
        """
        :type s: str
        :rtype: int
        """
        # first try
        # d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #
        # result = d[s[0]]
        # for i in range(1, len(s)):
        #     if d[s[i - 1]] >= d[s[i]]:
        #         result += d[s[i]]
        #     else:
        #         result = result + d[s[i]] - 2 * d[s[i - 1]]
        # return result
        
        # second try
        k = ['M', 'CM', 'D', "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        v = [1000, 900, 500, 400, 100,   90,   50,  40,   10,  9,  5,  4, 1]
        
        res = ""
        for i in range(len(v)):
            while v[i] <= num:
                res += k[i]
                num -= v[i]
        return res
       
        
if __name__=="__main__":
    print(Solution().intToRoman(3))
