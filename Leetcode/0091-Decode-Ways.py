class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (1 + len(s))

        dp[0] = 1

        for i in range(1, 1 + len(s)):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            if i != 1 and "10" <= s[i - 2: i] <= "26":
                dp[i] += dp[i - 2]
        return dp[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        if s[0] == "0":
            return 0
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
