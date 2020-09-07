class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # d = dict()
        # for word in wordDict:
        # 	g = d.setdefault(word, set())
        # 	ind = -1
        # 	while True:
        # 		try:
        # 			ind = s.index(word, ind+1)
        # 			g.add(ind)
        # 		except:
        # 			break
        # return d
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        ## i length
        ## break
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp.pop()


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    results = Solution().wordBreak(s, wordDict)
    print(results)
