class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in range(26):
        	d[chr(ord('A')+i)]=i+1

        res=0
        for i in range(len(s)):
        	res = res*26 + d[s[i]]
        return res

if __name__=="__main__":
    result = Solution().titleToNumber("ZY")
    print(result) 