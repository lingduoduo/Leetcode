class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str

        """
        ####brute force
        result = list()

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    result.append(sub)
        return len(result)


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s) - 1, -1, -1):  # 注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    result += 1
                    dp[i][j] = True
        return result


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for mid in range(2 * n - 1):
            left = mid // 2
            right = left + mid % 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res


if __name__ == "__main__":
    s = "abc"
    results = Solution().countSubstrings(s)
    print(results)
