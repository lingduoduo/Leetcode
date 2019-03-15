class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        result=d[s[0]]
        for i in range(1,len(s)):
        	if d[s[i-1]]>=d[s[i]]:
        		result += d[s[i]]
        	else:
        		result = result + d[s[i]] - 2*d[s[i-1]] 
        return result
        