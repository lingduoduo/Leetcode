class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Dictionary for memoization
        memo = {}
        def uniqueSubsequences(i, j):
            m, n = len(s), len(t)
            # Base case
            if i == m or j == n or m - i < n - j:
                return int(j == len(t))
            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i, j]
            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)
            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)
            # Cache the answer and return
            memo[i, j] = ans
            return ans
        return uniqueSubsequences(0, 0)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # Dynamic Programming table
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        # Base case initialization
        for j in range(n + 1):
            dp[m][j] = 0
        # Base case initialization
        for i in range(m + 1):
            dp[i][n] = 1
        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]
                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
