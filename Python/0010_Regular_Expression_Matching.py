class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (1 + n) for _ in range(1 + m)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Case 1: use zero occurrence of p[j - 2]
                    dp[i][j] = dp[i][j - 2]

                    # Case 2: use one or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

if __name__ == "__main__":
    results = Solution().isMatch(s="aa", p="a")
    print(results)
