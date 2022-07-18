class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = dict()
        for word in wordDict:
            g = d.setdefault(word, set())
            ind = -1
            while True:
                try:
                    ind = s.index(word, ind + 1)
                    g.add(ind)
                except:
                    break
        return d


class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp.pop()


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                l = len(w)
                if s[i - l: i] == w and dp[i - l]:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    results = Solution().wordBreak(s, wordDict)
    print(results)
