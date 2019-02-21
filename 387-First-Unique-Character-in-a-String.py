class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        
        for i in range(len(s)):
            try:
                d[s[i]]+=1
            except:
                d[s[i]]=1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


if __name__=="__main__":
    s = "leetcode"
    s = "loveleetcode"
    results = Solution().firstUniqChar(s)
    print(results)