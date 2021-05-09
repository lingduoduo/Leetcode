class Solution(object):
    def intToRoman(self, num: int) -> str:
        """
        :type s: str
        :rtype: int
        """
        ###second try
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
