class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0] * (1 + n2) for _ in range(1 + n1)]
        for i in range(1, 1 + n1):
            for j in range(1, 1 + n2):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return n1 + n2 - 2 * dp[-1][-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None)
        def steps(idx1, idx2):
            # if both pointers end
            if idx1 == len(word1) and idx2 == len(word2):
                return 0
            # if one word is longer
            if idx1 == len(word1) or idx2 == len(word2):
                return max(len(word1) - idx1, len(word2) - idx2)
            # if letters match move to the next index in both words
            if word1[idx1] == word2[idx2]:
                return steps(idx1 + 1, idx2 + 1)
            # if letters do not match we have three choices
            else:
                # remove the letter in word1 only
                case1 = 1 + steps(idx1 + 1, idx2)
                # remove the letter in word2 only
                case2 = 1 + steps(idx1, idx2 + 1)
                # remove both letters
                case3 = 2 + steps(idx1 + 1, idx2 + 1)
                return min(case1, case2, case2)

        return steps(0, 0)
