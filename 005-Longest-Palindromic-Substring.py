class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        print(s)
        if len(s)<=1:
            return s
        
        result = ""
        size = 0

        for i in range(len(s)):
        	indices = [k for k, x in enumerate(s) if x == s[i] and k>i]

        	for j in indices:
        		if s[i:(j+1)] == s[i:(j+1)][::-1] and (j-i+1) > size:
        			size = j-i+1
        			result = s[i:(j+1)]
        
        if size<2: return s[1]
        else: return result

if __name__ == "__main__":
    print(Solution().longestPalindrome("abbae"))
    print(Solution().longestPalindrome("bb"))
    print(Solution().longestPalindrome("cbbd"))
    print('Done')