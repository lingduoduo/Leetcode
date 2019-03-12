class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## Method 1
        if not s: 
            return True
        stack = list()
        for string in s:
        	if string in ['[', '{','(']:
        		stack.append(string)
        	else:
        		if len(stack)==0:
        			return False
        		last = stack.pop()
        		if string==']' and last!='[':
        			return False
        		elif string==')' and last!='(':
        			return False
        		elif string=='}' and last!='{':
        			return False
        return True if len(stack)==0 else False

        ## Method 2
        v=[]
        d={']':'[', ')':'(', '}':'{'}
        for i in range(len(s)):
            if s[i] in d.values():
                v.append(s[i])
            elif s[i] in d.keys():
                if len(v)==0 or d[s[i]]!=v.pop():
                    return False
        return len(v)==0

if __name__=="__main__":
	strings = "()[]{}"
	strings = "([)]"
	strings = "]"
	results = Solution().isValid(strings)
	print(results)