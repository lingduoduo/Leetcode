class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ###d = {}
        ###for i in range(26):
        ###    d[chr(ord('A') + i)] = i + 1
        #
        ###res = 0
        ###for i in range(len(s)):
        ###    res = res * 26 + d[s[i]]
        ###return res
        l = [chr(ord('A') + i) for i in range(26)]
        n = [i+1 for i in range(26)]
        d = dict(zip(l,n))
        
        res = 0
        for char in s:
            res = res*26 + d[char]
        return res
        


if __name__ == "__main__":
    result = Solution().titleToNumber("ZY")
    print(result)
