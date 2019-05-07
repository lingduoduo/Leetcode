class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        
        for i in range(min(len(s), len(t))):
            if s[i] in d1:
                d1[s[i]] += [i]
            else:
                d1[s[i]] = [i]
            
            if t[i] in d2:
                d2[t[i]] += [i]
            else:
                d2[t[i]] = [i]
            
            if s[i] != t[i]:
                return False
        
        pos1 = sorted([v for v in d1.values()])
        pos2 = sorted([v for v in d2.values()])
        
        return pos1 == pos2


if __name__ == "__main__":
    s = "ab"
    t = "ca"
    result = Solution().isIsomorphic(s, t)
    print(result)
