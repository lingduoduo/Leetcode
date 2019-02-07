class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return false
        pre = min(strs, key=len)

        for i in range(len(pre)):
        	for s in strs:
        		if s[i] != pre[i]:
        			return pre[:i]
        return pre
