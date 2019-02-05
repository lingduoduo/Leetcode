class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        curr = sorted(words)

        result = ""

        for curr in words:
        	isIn = True
        	for i in range(1,len(curr)):
        		if curr[:i] not in words:
        			isIn = False
        			break
        	if isIn:
        		if not result or len(result)<len(curr):
        			result = curr
        		elif len(curr) == len(result) and result>curr:
        			result = curr
        return result
