class Solution:
    def removePalindromeSub(self, s: str) -> int:
        dp = [0]*len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            for j in range(i):
                if dp[j] = 1 and s[j:i] = s[j:i:-1]:
                    dp[i] = dp[j+1]
                