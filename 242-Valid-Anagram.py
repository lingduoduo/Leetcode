import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1=collections.Counter(s)
        c2=collections.Counter(t)
        if c1==c2:
        	return True
        else:
        	return False

if __name__=="__main__":
    s = "anagram"
    t = "nagaram"
    results = Solution().isAnagram(s, t)
    print(results)
