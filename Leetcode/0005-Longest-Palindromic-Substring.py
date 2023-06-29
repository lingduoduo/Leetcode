class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        i = 0
        start = 0
        size = 0
        while i < n:
            if n - i <= size // 2:
                break
            left = right = i
            while right < n - 1 and s[right] == s[right + 1]:
                right += 1
            i = right + 1
            while right < n - 1 and left > 0 and s[right + 1] == s[left - 1]:
                right += 1
                left -= 1
            cur = right - left + 1
            if cur > size:
                start = left
                size = cur
        return s[start : start + size]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res = [i, j]

        i, j = res
        return s[i : j + 1]


if __name__ == "__main__":
    print(Solution().longestPalindrome("abbae"))
    # print(Solution().longestPalindrome("bb"))
    # print(Solution().longestPalindrome("cbbd"))
    # print('Done')
