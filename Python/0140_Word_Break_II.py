class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i):
            if i in memo:
                return memo[i]
            res = []
            for j in range(i, len(s)):
                prefix = s[i : j + 1]
                if prefix in wordDict:
                    tmp = dfs(j + 1)
                    for word in tmp:
                        res.append((prefix + " " + word).strip())
            memo[i] = res
            return res

        wordDict = set(wordDict)
        memo = {len(s): [""]}
        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        # @lru_cache(maxsize=None)    # alternative memoization solution
        def dfs(s):
            """return list of word lists"""
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s) + 1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in dfs(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        dfs(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        for j in range(1, len(s) + 1):
            sublist = []
            for i in range(j):
                if s[i:j] in wordSet:
                    for words in dp[i]:
                        sublist.append((words + " " + s[i:j]).strip())
            dp[j] = sublist
        return dp[-1]
