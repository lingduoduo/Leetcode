import collections


class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for word in strs:
            cnt = collections.Counter(word)
            for i in range(m, cnt["0"] - 1, -1):
                for j in range(n, cnt["1"] - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt["0"]][j - cnt["1"]] + 1)
        return dp[m][n]


class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for word in strs:
            zeros = word.count("0")
            ones = word.count("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[-1][-1]


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    res = Solution().findMaxForm(strs, m, n)
    print(res)

    strs = ["10", "0", "1"]
    m = 1
    n = 1
    res = Solution().findMaxForm(strs, m, n)
    print(res)
