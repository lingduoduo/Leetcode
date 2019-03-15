class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #return haystack.find(needle)
        m=len(needle)

        for i in range(len(haystack)-m+1):
        	if haystack[i:i+m] == needle:
        		return i
        return -1
