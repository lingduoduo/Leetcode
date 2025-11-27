class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        len_s = len(s)

        i = 0
        for char in t:
            if char == s[i]:
                i += 1
            if i == len_s:
                return True
        return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        if dp[-1][-1] == len(s):
            return True
        return False
