class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        
        isPalindrome = lambda input: input == input[::-1]
        while start<end :
        	if s[start] != s[end]:
        		case1 = s[:start]+s[start+1:]
        		case2 = s[:end]+s[end+1:]
        		return isPalindrome(case1) or isPalindrome(case2)
        	start+=1
        	end-=1
        return True
        