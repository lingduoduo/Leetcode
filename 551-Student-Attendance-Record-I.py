class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for c in s:
        	if c == 'A':
        		a+=1
        	if c == 'L':
        		l+=1
        	else:
        		if l < 3:
        			l = 0
        if a>1 or l>2:
        	return False
        else:
        	return True


if __name__=="__main__":
	s = "LLLALL"
	result = Solution().checkRecord(s)
	print(result)