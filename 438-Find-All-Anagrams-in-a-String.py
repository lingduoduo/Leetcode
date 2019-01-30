class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        l = len(p)
        vp = [0]*26
        vs = [0]*26
        results = list()
        for cha in p:
            vp[ord(cha) - ord('a')] += 1
        for i in range(n):
            if (i>=l): vs[ord(s[i-l]) - ord('a')] -= 1
            vs[ord(s[i]) - ord('a')] += 1
            if vp == vs:
                results.append(i+1-l)
        return results

