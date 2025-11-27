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
        dp = [[False] * len(s) for _ in range(len(s))]
        maxlenth = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    if j - i <= 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxlenth:
                    maxlenth = j - i + 1
                    left = i
                    right = j
        return s[left : right + 1]


if __name__ == "__main__":
    print(Solution().longestPalindrome("abbae"))
    # print(Solution().longestPalindrome("bb"))
    # print(Solution().longestPalindrome("cbbd"))
    # print('Done')
