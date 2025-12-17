class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        # dp[left][right] = minimum deletions needed to make s[left:right+1] a palindrome
        dp = [[0] * n for _ in range(n)]

        # Build from shorter substrings to longer ones
        for left in range(n - 1, -1, -1):
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1]  # inner substring
                else:
                    delete_left = 1 + dp[left + 1][right]
                    delete_right = 1 + dp[left][right - 1]
                    dp[left][right] = min(delete_left, delete_right)

        return dp[0][n - 1] <= k
